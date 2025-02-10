from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    parent_collection_name: str,
    id: int,
    *,
    token: str,
    derived_collection_name: str,
    derived_collection_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["derived_collection_name"] = derived_collection_name

    params["derived_collection_id"] = derived_collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/biocollections/{parent_collection_name}/{id}/get_derived_items",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if response.status_code == 404:
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
    parent_collection_name: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    derived_collection_name: str,
    derived_collection_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Get the derived items of a generic collection item

    Args:
        parent_collection_name (str):
        id (int):
        token (str):
        derived_collection_name (str):
        derived_collection_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parent_collection_name=parent_collection_name,
        id=id,
        token=token,
        derived_collection_name=derived_collection_name,
        derived_collection_id=derived_collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    parent_collection_name: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    derived_collection_name: str,
    derived_collection_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Get the derived items of a generic collection item

    Args:
        parent_collection_name (str):
        id (int):
        token (str):
        derived_collection_name (str):
        derived_collection_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parent_collection_name=parent_collection_name,
        id=id,
        token=token,
        derived_collection_name=derived_collection_name,
        derived_collection_id=derived_collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
