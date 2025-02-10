from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_element import AddElement
from ...models.add_plate_element import AddPlateElement
from ...types import Response


def _get_kwargs(
    *,
    body: Union["AddElement", "AddPlateElement"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/elements",
    }

    _body: dict[str, Any]
    if isinstance(body, AddElement):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 201:
        return None
    if response.status_code == 422:
        return None
    if response.status_code == 401:
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AddElement", "AddPlateElement"],
) -> Response[Any]:
    """Add element

     This endpoint creates an element within a specific section of an ELN or knowledgebase item.

    To add an element, specify its type and the corresponding section ID,
    Once created, the element is automatically integrated and displayed in the designated section.

    Args:
        body (Union['AddElement', 'AddPlateElement']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AddElement", "AddPlateElement"],
) -> Response[Any]:
    """Add element

     This endpoint creates an element within a specific section of an ELN or knowledgebase item.

    To add an element, specify its type and the corresponding section ID,
    Once created, the element is automatically integrated and displayed in the designated section.

    Args:
        body (Union['AddElement', 'AddPlateElement']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
