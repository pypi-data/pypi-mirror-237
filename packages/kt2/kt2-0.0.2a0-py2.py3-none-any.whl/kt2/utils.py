from contextlib import contextmanager
from enum import Enum
from functools import wraps
from logging import Logger
from typing import Any, Optional, Type, cast

import httpx
from fhir.resources.R4B.bundle import Bundle
from pydantic import BaseModel

from kt2.errors import KoppeltaalApiError


# HTTP methods helper
class Methods(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


# Decorator for binding fhir urls to client methods and set expected response model
def url(
    url,
    response_model: Type[BaseModel],
    many: bool = False,
):
    def inner(func):
        @wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            base_url = self.fhir_url
            kwargs['url'] = base_url + url

            # request token
            if not self.token or self.token.is_expired:
                await self.get_access_token()

            # make request
            response = await func(self, *args, **kwargs)

            # Response is empty, so we handling update, create or delete
            if not response:
                return None

            if many:
                # handle Bundle response; cast as Bundle than map to response model
                data = cast(Bundle, response)
                bundle = Bundle(**data)
                self.logger.info(data)

                if not bool(bundle.total):
                    return []

                return [cast(response_model, entry.resource) for entry in bundle.entry]

            data = cast(response_model, response)
            return response_model(**data)

        return async_wrapper

    return inner


@contextmanager
def handle_response(response: httpx.Response, method: Methods, logger: Logger):
    exception_raised = None

    try:
        response.raise_for_status()
    except (
        httpx.ConnectError,
        httpx.RemoteProtocolError,
        httpx.TransportError,
    ) as exception:
        logger.error(f"Connection error detected: {exception}")

    except httpx.RequestError as exception:
        exception_raised = KoppeltaalApiError(
            f'An error occurred while requesting {exception.request.url!r}'
        )
    except httpx.HTTPStatusError as exception:
        exception_raised = KoppeltaalApiError(
            f'An error occurred while requesting {exception.request.url!r}: '
            f'{exception.response.status_code}'
        )

    if exception_raised:
        raise exception_raised

    logger.info(f"{method.name} - {response.request.url} - {response.status_code}")

    yield response


async def make_request(
    client: httpx.AsyncClient,
    *,
    method: Methods,
    url: str,
    logger: Any,
    params: Optional[Any] = None,
    data: Optional[Any] = None,
):
    """Make Httpx request and handle errors"""

    if method == Methods.GET:
        response: httpx.Response = await client.get(url=url, params=params)
        with handle_response(response, method, logger):
            return response.json()
    elif method == Methods.DELETE:
        response = await client.delete(url=url, params=params)
        with handle_response(response, method, logger):
            return None
    elif method == Methods.PUT:
        response = await client.put(url=url, params=params, data=data)
        with handle_response(response, method, logger):
            return None
    elif method == Methods.POST:
        response = await client.post(url=url, params=params, data=data)
        with handle_response(response, method, logger):
            return None

    return None
