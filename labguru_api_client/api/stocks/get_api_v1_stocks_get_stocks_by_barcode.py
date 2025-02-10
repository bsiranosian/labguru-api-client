from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ok import OK
from ...models.unauthorized import Unauthorized
from ...types import UNSET, Response


def _get_kwargs(
    *,
    token: str,
    input_: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["input"] = input_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stocks/get_stocks_by_barcode",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[OK, Unauthorized]]:
    if response.status_code == 200:
        response_200 = OK.from_dict(response.json())

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
) -> Response[Union[OK, Unauthorized]]:
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
    input_: str,
) -> Response[Union[OK, Unauthorized]]:
    """Get stock by barcode/id

    Args:
        token (str):
        input_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OK, Unauthorized]]
    """

    kwargs = _get_kwargs(
        token=token,
        input_=input_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    input_: str,
) -> Optional[Union[OK, Unauthorized]]:
    """Get stock by barcode/id

    Args:
        token (str):
        input_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OK, Unauthorized]
    """

    return sync_detailed(
        client=client,
        token=token,
        input_=input_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    input_: str,
) -> Response[Union[OK, Unauthorized]]:
    """Get stock by barcode/id

    Args:
        token (str):
        input_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OK, Unauthorized]]
    """

    kwargs = _get_kwargs(
        token=token,
        input_=input_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    input_: str,
) -> Optional[Union[OK, Unauthorized]]:
    """Get stock by barcode/id

    Args:
        token (str):
        input_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OK, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
            input_=input_,
        )
    ).parsed
