# copyright 2022-2023 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact https://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import logging
from functools import partial
from enum import Enum

from cubicweb import AuthenticationError
from cubicweb.schema_exporters import JSONSchemaExporter
from cubicweb.sobjects.services import StatsService, GcStatsService
from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.response import Response
from pyramid.security import remember
from pyramid.settings import asbool

from cubicweb_api.auth.jwt_auth import setup_jwt
from cubicweb_api.constants import (
    API_ROUTE_NAME_PREFIX,
)
from cubicweb_api.openapi.openapi import setup_openapi
from cubicweb_api.util import get_cw_repo
from cubicweb_api.transaction import Transaction

log = logging.getLogger(__name__)


class ApiRoutes(Enum):
    """
    All the available routes as listed in the openapi/openapi_template.yml file.
    """

    schema = "schema"
    rql = "rql"
    transaction = "transaction"
    login = "login"
    current_user = "current_user"
    siteinfo = "siteinfo"
    help = "help"


def get_route_name(route_name: ApiRoutes) -> str:
    """
    Generates a unique route name using the api
    prefix to prevent clashes with routes from other cubes.

    :param route_name: The route name base
    :return: The generated route name
    """
    return f"{API_ROUTE_NAME_PREFIX}{route_name.value}"


def schema_view(request: Request):
    """
    See the openapi/openapi_template.yml
    file for more information about this route.
    """
    repo = get_cw_repo(request)
    exporter = JSONSchemaExporter()
    exported_schema = exporter.export_as_dict(repo.schema)
    return exported_schema


def rql_view(request: Request):
    """
    See the openapi/openapi_template.yml
    file for more information about this route.
    """
    request_params = request.openapi_validated.body
    query: str = request_params["query"]
    params: dict = request_params["params"]
    rset = request.cw_cnx.execute(query, params).rows
    request.cw_cnx.commit()
    return rset


def transaction_view(request: Request):
    """
    See the openapi/openapi_template.yml
    file for more information about this route.
    """
    queries = request.openapi_validated.body
    transaction = Transaction(queries)
    rsets = [rset.rows for rset in transaction.execute(request.cw_cnx)]
    return rsets


def login_view(request: Request):
    """
    See the openapi/openapi_template.yml
    file for more information about this route.
    """
    request_params = request.openapi_validated.body
    login: str = request_params["login"]
    pwd: str = request_params["password"]

    repo = get_cw_repo(request)
    with repo.internal_cnx() as cnx:
        try:
            cwuser = repo.authenticate_user(cnx, login, password=pwd)
        except AuthenticationError:
            raise AuthenticationError("Invalid credentials")

        headers = remember(
            request,
            cwuser.eid,
        )
        return Response(headers=headers, status=204)


def current_user_view(request: Request) -> dict:
    """
    See the openapi/openapi_template.yml
    file for more information about this route.
    """
    user = request.cw_cnx.user
    return {"eid": user.eid, "login": user.login, "dcTitle": user.dc_title()}


def siteinfo_view(request: Request):
    """
    display debugging information about the current website
    """
    repo = get_cw_repo(request)
    version_configuration = repo.get_versions()

    pyvalue = {
        "config_type": repo.vreg.config.name,
        "config_mode": repo.vreg.config.mode,
        "instance_home": repo.vreg.config.apphome,
        "cubicweb": version_configuration.get("cubicweb", "no version configuration"),
        "cubes": {
            pk.replace("system.version.", ""): version
            for pk, version in request.cw_cnx.execute(
                "Any K,V WHERE P is CWProperty, P value V, P pkey K, "
                'P pkey ~="system.version.%"',
                build_descr=False,
            )
        },
        "base_url": repo.config["base-url"],
        "datadir_url": getattr(repo.vreg.config, "datadir_url", None),
    }

    return {
        "info": {
            "pyvalue": pyvalue,
            "stats": StatsService(request.cw_cnx).call(),
        },
        "registry": {
            x: {a: [str(klass) for klass in b] for a, b in y.items()}
            for x, y in repo.vreg.items()
        },
        "gc": GcStatsService(request.cw_cnx).call(),
    }


def includeme(config: Configurator):
    enable_login = asbool(
        config.registry.settings.get("cubicweb_api.enable_login_route", False)
    )
    if enable_login:
        setup_jwt(config)

    setup_openapi(config, enable_login=enable_login)
    config.pyramid_openapi3_register_routes()

    view_defaults = dict(
        request_method="POST",
        renderer="cubicweb_api_json",
        require_csrf=False,
        openapi=True,
        use_api_exceptions=True,
        anonymous_or_connected=True,
    )
    add_view = partial(config.add_view, **view_defaults)

    add_view(
        view=schema_view,
        route_name=get_route_name(ApiRoutes.schema),
        request_method="GET",
    )
    add_view(
        view=rql_view,
        route_name=get_route_name(ApiRoutes.rql),
    )

    add_view(
        view=transaction_view,
        route_name=get_route_name(ApiRoutes.transaction),
    )

    if enable_login:
        add_view(
            view=login_view,
            route_name=get_route_name(ApiRoutes.login),
            anonymous_or_connected=None,
        )

    add_view(
        view=current_user_view,
        route_name=get_route_name(ApiRoutes.current_user),
        request_method="GET",
    )

    add_view(
        view=siteinfo_view,
        route_name=get_route_name(ApiRoutes.siteinfo),
        request_method="GET",
    )
