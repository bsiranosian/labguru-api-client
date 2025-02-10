from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    knowledgbase_collection: str,
    *,
    token: str,
    page: Union[Unset, int] = 1,
    meta: Union[Unset, str] = "true",
    kendo: str = "true",
    filterlogic: str = "and",
    filterfilters0field: str,
    filterfilters0operator: str,
    filterfilters0value: str,
    tag_ids: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["page"] = page

    params["meta"] = meta

    params["kendo"] = kendo

    params["filter[logic]"] = filterlogic

    params["filter[filters][0][field]"] = filterfilters0field

    params["filter[filters][0][operator]"] = filterfilters0operator

    params["filter[filters][0][value]"] = filterfilters0value

    params["tag_ids"] = tag_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/{knowledgbase_collection}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledgbase_collection: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    page: Union[Unset, int] = 1,
    meta: Union[Unset, str] = "true",
    kendo: str = "true",
    filterlogic: str = "and",
    filterfilters0field: str,
    filterfilters0operator: str,
    filterfilters0value: str,
    tag_ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Filter knowledgbase items

    Args:
        knowledgbase_collection (str):
        token (str):
        page (Union[Unset, int]):  Default: 1.
        meta (Union[Unset, str]):  Default: 'true'.
        kendo (str):  Default: 'true'.
        filterlogic (str):  Default: 'and'.
        filterfilters0field (str):
        filterfilters0operator (str):
        filterfilters0value (str):
        tag_ids (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        knowledgbase_collection=knowledgbase_collection,
        token=token,
        page=page,
        meta=meta,
        kendo=kendo,
        filterlogic=filterlogic,
        filterfilters0field=filterfilters0field,
        filterfilters0operator=filterfilters0operator,
        filterfilters0value=filterfilters0value,
        tag_ids=tag_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    knowledgbase_collection: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    page: Union[Unset, int] = 1,
    meta: Union[Unset, str] = "true",
    kendo: str = "true",
    filterlogic: str = "and",
    filterfilters0field: str,
    filterfilters0operator: str,
    filterfilters0value: str,
    tag_ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Filter knowledgbase items

    Args:
        knowledgbase_collection (str):
        token (str):
        page (Union[Unset, int]):  Default: 1.
        meta (Union[Unset, str]):  Default: 'true'.
        kendo (str):  Default: 'true'.
        filterlogic (str):  Default: 'and'.
        filterfilters0field (str):
        filterfilters0operator (str):
        filterfilters0value (str):
        tag_ids (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        knowledgbase_collection=knowledgbase_collection,
        token=token,
        page=page,
        meta=meta,
        kendo=kendo,
        filterlogic=filterlogic,
        filterfilters0field=filterfilters0field,
        filterfilters0operator=filterfilters0operator,
        filterfilters0value=filterfilters0value,
        tag_ids=tag_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
