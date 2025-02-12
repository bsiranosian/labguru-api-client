from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_flags_id_response_401 import GetApiV1FlagsIdResponse401
from ...models.get_api_v1_flags_id_response_404 import GetApiV1FlagsIdResponse404
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    token: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/flags/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 404:
        response_404 = GetApiV1FlagsIdResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = GetApiV1FlagsIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]:
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
    token: str,
) -> Response[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]:
    """Get flag by id

     Get a flag by ID.

    Args:
        id (int):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
) -> Optional[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]:
    """Get flag by id

     Get a flag by ID.

    Args:
        id (int):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]
    """

    return sync_detailed(
        id=id,
        client=client,
        token=token,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
) -> Response[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]:
    """Get flag by id

     Get a flag by ID.

    Args:
        id (int):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
) -> Optional[Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]]:
    """Get flag by id

     Get a flag by ID.

    Args:
        id (int):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1FlagsIdResponse401, GetApiV1FlagsIdResponse404]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            token=token,
        )
    ).parsed
