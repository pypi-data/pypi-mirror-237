from functools import wraps
from importlib.metadata import version
from typing import Callable, Concatenate, ParamSpec, TypeVar

import requests
import seaplane_framework.api
from seaplane_framework.api import ApiClient

from seaplane.api.api_http import SDK_HTTP_ERROR_CODE
from seaplane.api.token_api import TokenAPI
from seaplane.config import config
from seaplane.errors import HTTPError
from seaplane.logs import log

T = TypeVar("T")

_R = TypeVar("_R")
_P = ParamSpec("_P")
_SelfType = TypeVar("_SelfType")


# (self, token, *args, **kwargs) -> ret ==>  (self, *args, **kwargs) -> ret
#
# The type annotation is complicated because of PEP-612 only allowing us to put
# arguments at the front of wrapped functions, combined with methods always
# taking `self` as the first argument. We double-wrap using an explicit
# `_SelfType` so the token is passed as the first non-`self` parameter.
def method_with_token(
    func: Callable[Concatenate[_SelfType, str, _P], _R]
) -> Callable[Concatenate[_SelfType, _P], _R]:
    """
    A decorator around class methods that need JWTs.

    The JWT will be passed in as the first parameter.

    The JWTs will be pulled from the global `config` wrapper. The wrapped
    function will be retried if the token needs to be refreshed.
    """

    @wraps(func)
    def _inner(this: _SelfType, /, *args: _P.args, **kwargs: _P.kwargs) -> _R:
        token_api = config._token_api
        try:
            return func(this, token_api.get_token(), *args, **kwargs)
        except HTTPError as e:
            _renew_if_failed(token_api, e)
            return func(this, token_api.get_token(), *args, **kwargs)
        except requests.exceptions.RequestException as err:
            _renew_if_failed(token_api, _map_request_exception(err))
            return func(this, token_api.get_token(), *args, **kwargs)

    return _inner


def with_token(func: Callable[Concatenate[str, _P], _R]) -> Callable[_P, _R]:
    """
    A decorator around bare functions that need JWTs.

    The JWT will be passed in as the first parameter.

    The JWTs will be pulled from the global `config` wrapper. The wrapped
    function will be retried if the token needs to be refreshed.
    """

    @wraps(func)
    def _inner(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        token_api = config._token_api
        try:
            return func(token_api.get_token(), *args, **kwargs)
        except HTTPError as e:
            _renew_if_failed(token_api, e)
            return func(token_api.get_token(), *args, **kwargs)
        except requests.exceptions.RequestException as err:
            _renew_if_failed(token_api, _map_request_exception(err))
            return func(token_api.get_token(), *args, **kwargs)

    return _inner


def _renew_if_failed(token_api: TokenAPI, http_error: HTTPError) -> None:
    """
    Attempts to renew a token if the given error calls for it.
    """
    if http_error.status != 401 or not token_api.auto_renew:
        raise http_error
    log.info("Auto-Renew, renewing the token...")
    token_api.renew_token()


def _map_request_exception(err: requests.exceptions.RequestException) -> HTTPError:
    """
    Maps a raw `requests` exception into a Seaplane `HTTPError`.
    """
    log.error(f"Request exception: {str(err)}")
    status_code: int = SDK_HTTP_ERROR_CODE
    if err.response:
        status_code = err.response.status_code
    return HTTPError(status_code, str(err))


def get_pdk_client(access_token: str) -> ApiClient:
    """
    Constructs a Seaplane PDK ApiClient from the given access token.
    """

    pdk_config = config.get_platform_configuration()
    pdk_config.access_token = access_token
    client = ApiClient(pdk_config)
    client.set_default_header("X-Seaplane-Sdk-Version", version("seaplane"))
    client.set_default_header("X-Seaplane-Pdk-Version", seaplane_framework.api.__version__)
    return client
