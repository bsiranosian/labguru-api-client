from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_api_v1_links_id_response_422 import PutApiV1LinksIdResponse422
from ...models.unauthorized import Unauthorized
from ...models.update_link import UpdateLink
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: UpdateLink,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/links/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 422:
        response_422 = PutApiV1LinksIdResponse422.from_dict(response.json())

        return response_422
    if response.status_code == 401:
        response_401 = Unauthorized.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLink,
) -> Response[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]:
    """Update a link

    Args:
        id (int):
        body (UpdateLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLink,
) -> Optional[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]:
    """Update a link

    Args:
        id (int):
        body (UpdateLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PutApiV1LinksIdResponse422, Unauthorized]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLink,
) -> Response[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]:
    """Update a link

    Args:
        id (int):
        body (UpdateLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLink,
) -> Optional[Union[Any, PutApiV1LinksIdResponse422, Unauthorized]]:
    """Update a link

    Args:
        id (int):
        body (UpdateLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PutApiV1LinksIdResponse422, Unauthorized]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
