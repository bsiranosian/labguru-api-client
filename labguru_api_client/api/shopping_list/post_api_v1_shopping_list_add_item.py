from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_custom_item import AddCustomItem
from ...models.add_item import AddItem
from ...models.post_api_v1_shopping_list_add_item_response_200 import PostApiV1ShoppingListAddItemResponse200
from ...models.post_api_v1_shopping_list_add_item_response_422 import PostApiV1ShoppingListAddItemResponse422
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    *,
    body: Union["AddCustomItem", "AddItem"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/shopping_list/add_item",
    }

    _body: dict[str, Any]
    if isinstance(body, AddItem):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]:
    if response.status_code == 200:
        response_200 = PostApiV1ShoppingListAddItemResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = PostApiV1ShoppingListAddItemResponse422.from_dict(response.json())

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
) -> Response[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AddCustomItem", "AddItem"],
) -> Response[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]:
    """Add item

     This endpoint allows for adding standard or custom commercial items to the shopping list. It
    supports two types of item additions:
    1. **Standard Item Addition**: Using the `addItem` schema for predefined commercial item types.

    2. **Custom Item Addition**: Using the `addCustomItem` schema for user-defined commercial items and
    collections.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['AddCustomItem', 'AddItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]
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
    body: Union["AddCustomItem", "AddItem"],
) -> Optional[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]:
    """Add item

     This endpoint allows for adding standard or custom commercial items to the shopping list. It
    supports two types of item additions:
    1. **Standard Item Addition**: Using the `addItem` schema for predefined commercial item types.

    2. **Custom Item Addition**: Using the `addCustomItem` schema for user-defined commercial items and
    collections.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['AddCustomItem', 'AddItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AddCustomItem", "AddItem"],
) -> Response[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]:
    """Add item

     This endpoint allows for adding standard or custom commercial items to the shopping list. It
    supports two types of item additions:
    1. **Standard Item Addition**: Using the `addItem` schema for predefined commercial item types.

    2. **Custom Item Addition**: Using the `addCustomItem` schema for user-defined commercial items and
    collections.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['AddCustomItem', 'AddItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AddCustomItem", "AddItem"],
) -> Optional[Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]]:
    """Add item

     This endpoint allows for adding standard or custom commercial items to the shopping list. It
    supports two types of item additions:
    1. **Standard Item Addition**: Using the `addItem` schema for predefined commercial item types.

    2. **Custom Item Addition**: Using the `addCustomItem` schema for user-defined commercial items and
    collections.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['AddCustomItem', 'AddItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiV1ShoppingListAddItemResponse200, PostApiV1ShoppingListAddItemResponse422, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
