from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_flag import CreateFlag
from ...models.post_api_v1_flags_response_200 import PostApiV1FlagsResponse200
from ...models.post_api_v1_flags_response_401 import PostApiV1FlagsResponse401
from ...models.post_api_v1_flags_response_422 import PostApiV1FlagsResponse422
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFlag,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/flags",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]:
    if response.status_code == 200:
        response_200 = PostApiV1FlagsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = PostApiV1FlagsResponse422.from_dict(response.json())

        return response_422
    if response.status_code == 401:
        response_401 = PostApiV1FlagsResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFlag,
) -> Response[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]:
    """Create a Flag

     Create a flag.

    Args:
        body (CreateFlag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFlag,
) -> Optional[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]:
    """Create a Flag

     Create a flag.

    Args:
        body (CreateFlag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFlag,
) -> Response[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]:
    """Create a Flag

     Create a flag.

    Args:
        body (CreateFlag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFlag,
) -> Optional[Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]]:
    """Create a Flag

     Create a flag.

    Args:
        body (CreateFlag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiV1FlagsResponse200, PostApiV1FlagsResponse401, PostApiV1FlagsResponse422]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
