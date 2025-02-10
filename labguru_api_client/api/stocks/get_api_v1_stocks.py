from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.index_filtering import IndexFiltering
from ...models.unauthorized import Unauthorized
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    token: str,
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = "true",
    stockable_type: Union[Unset, str] = UNSET,
    stockable_id: Union[Unset, int] = UNSET,
    filter_: Union[Unset, "IndexFiltering"] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["page"] = page

    params["meta"] = meta

    params["stockable_type"] = stockable_type

    params["stockable_id"] = stockable_id

    json_filter_: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict()
    if not isinstance(json_filter_, Unset):
        params.update(json_filter_)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stocks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Unauthorized]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 401:
        response_401 = Unauthorized.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Unauthorized]]:
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
    meta: Union[Unset, str] = "true",
    stockable_type: Union[Unset, str] = UNSET,
    stockable_id: Union[Unset, int] = UNSET,
    filter_: Union[Unset, "IndexFiltering"] = UNSET,
) -> Response[Union[Any, Unauthorized]]:
    """List all stocks in your account

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):  Default: 'true'.
        stockable_type (Union[Unset, str]):
        stockable_id (Union[Unset, int]):
        filter_ (Union[Unset, IndexFiltering]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Unauthorized]]
    """

    kwargs = _get_kwargs(
        token=token,
        page=page,
        meta=meta,
        stockable_type=stockable_type,
        stockable_id=stockable_id,
        filter_=filter_,
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
    meta: Union[Unset, str] = "true",
    stockable_type: Union[Unset, str] = UNSET,
    stockable_id: Union[Unset, int] = UNSET,
    filter_: Union[Unset, "IndexFiltering"] = UNSET,
) -> Optional[Union[Any, Unauthorized]]:
    """List all stocks in your account

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):  Default: 'true'.
        stockable_type (Union[Unset, str]):
        stockable_id (Union[Unset, int]):
        filter_ (Union[Unset, IndexFiltering]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Unauthorized]
    """

    return sync_detailed(
        client=client,
        token=token,
        page=page,
        meta=meta,
        stockable_type=stockable_type,
        stockable_id=stockable_id,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = "true",
    stockable_type: Union[Unset, str] = UNSET,
    stockable_id: Union[Unset, int] = UNSET,
    filter_: Union[Unset, "IndexFiltering"] = UNSET,
) -> Response[Union[Any, Unauthorized]]:
    """List all stocks in your account

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):  Default: 'true'.
        stockable_type (Union[Unset, str]):
        stockable_id (Union[Unset, int]):
        filter_ (Union[Unset, IndexFiltering]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Unauthorized]]
    """

    kwargs = _get_kwargs(
        token=token,
        page=page,
        meta=meta,
        stockable_type=stockable_type,
        stockable_id=stockable_id,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    page: Union[Unset, int] = UNSET,
    meta: Union[Unset, str] = "true",
    stockable_type: Union[Unset, str] = UNSET,
    stockable_id: Union[Unset, int] = UNSET,
    filter_: Union[Unset, "IndexFiltering"] = UNSET,
) -> Optional[Union[Any, Unauthorized]]:
    """List all stocks in your account

    Args:
        token (str):
        page (Union[Unset, int]):
        meta (Union[Unset, str]):  Default: 'true'.
        stockable_type (Union[Unset, str]):
        stockable_id (Union[Unset, int]):
        filter_ (Union[Unset, IndexFiltering]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
            page=page,
            meta=meta,
            stockable_type=stockable_type,
            stockable_id=stockable_id,
            filter_=filter_,
        )
    ).parsed
