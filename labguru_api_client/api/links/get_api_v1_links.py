from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_links_response_404 import GetApiV1LinksResponse404
from ...models.unauthorized import Unauthorized
from ...types import UNSET, Response


def _get_kwargs(
    *,
    token: str,
    item_uuid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["item_uuid"] = item_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/links",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiV1LinksResponse404, Unauthorized]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 404:
        response_404 = GetApiV1LinksResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = Unauthorized.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetApiV1LinksResponse404, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    item_uuid: str,
) -> Response[Union[Any, GetApiV1LinksResponse404, Unauthorized]]:
    """Get link by uuid

    Args:
        token (str):
        item_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1LinksResponse404, Unauthorized]]
    """

    kwargs = _get_kwargs(
        token=token,
        item_uuid=item_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    item_uuid: str,
) -> Optional[Union[Any, GetApiV1LinksResponse404, Unauthorized]]:
    """Get link by uuid

    Args:
        token (str):
        item_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1LinksResponse404, Unauthorized]
    """

    return sync_detailed(
        client=client,
        token=token,
        item_uuid=item_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    item_uuid: str,
) -> Response[Union[Any, GetApiV1LinksResponse404, Unauthorized]]:
    """Get link by uuid

    Args:
        token (str):
        item_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1LinksResponse404, Unauthorized]]
    """

    kwargs = _get_kwargs(
        token=token,
        item_uuid=item_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    item_uuid: str,
) -> Optional[Union[Any, GetApiV1LinksResponse404, Unauthorized]]:
    """Get link by uuid

    Args:
        token (str):
        item_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1LinksResponse404, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
            item_uuid=item_uuid,
        )
    ).parsed
