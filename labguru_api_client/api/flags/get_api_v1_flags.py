from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_flags_response_404 import GetApiV1FlagsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    token: str,
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["page"] = page

    params["meta"] = meta

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/flags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiV1FlagsResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 404:
        response_404 = GetApiV1FlagsResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetApiV1FlagsResponse404]]:
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
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiV1FlagsResponse404]]:
    """List all flags in your account

     List all flags.

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1FlagsResponse404]]
    """

    kwargs = _get_kwargs(
        token=token,
        page=page,
        meta=meta,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiV1FlagsResponse404]]:
    """List all flags in your account

     List all flags.

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1FlagsResponse404]
    """

    return sync_detailed(
        client=client,
        token=token,
        page=page,
        meta=meta,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiV1FlagsResponse404]]:
    """List all flags in your account

     List all flags.

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1FlagsResponse404]]
    """

    kwargs = _get_kwargs(
        token=token,
        page=page,
        meta=meta,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiV1FlagsResponse404]]:
    """List all flags in your account

     List all flags.

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1FlagsResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
            page=page,
            meta=meta,
        )
    ).parsed
