from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_consume_sample_pooling_event import CreateConsumeSamplePoolingEvent
from ...models.create_custom_sample_pooling_event import CreateCustomSamplePoolingEvent
from ...models.create_fixed_sample_pooling_event import CreateFixedSamplePoolingEvent
from ...models.post_api_v1_pool_events_response_200 import PostApiV1PoolEventsResponse200
from ...models.post_api_v1_pool_events_response_401 import PostApiV1PoolEventsResponse401
from ...models.post_api_v1_pool_events_response_404 import PostApiV1PoolEventsResponse404
from ...models.post_api_v1_pool_events_response_422 import PostApiV1PoolEventsResponse422
from ...types import Response


def _get_kwargs(
    *,
    body: Union["CreateConsumeSamplePoolingEvent", "CreateCustomSamplePoolingEvent", "CreateFixedSamplePoolingEvent"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/pool_events",
    }

    _body: dict[str, Any]
    if isinstance(body, CreateFixedSamplePoolingEvent):
        _body = body.to_dict()
    elif isinstance(body, CreateCustomSamplePoolingEvent):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        PostApiV1PoolEventsResponse200,
        PostApiV1PoolEventsResponse401,
        PostApiV1PoolEventsResponse404,
        PostApiV1PoolEventsResponse422,
    ]
]:
    if response.status_code == 200:
        response_200 = PostApiV1PoolEventsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = PostApiV1PoolEventsResponse422.from_dict(response.json())

        return response_422
    if response.status_code == 401:
        response_401 = PostApiV1PoolEventsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = PostApiV1PoolEventsResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        PostApiV1PoolEventsResponse200,
        PostApiV1PoolEventsResponse401,
        PostApiV1PoolEventsResponse404,
        PostApiV1PoolEventsResponse422,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["CreateConsumeSamplePoolingEvent", "CreateCustomSamplePoolingEvent", "CreateFixedSamplePoolingEvent"],
) -> Response[
    Union[
        PostApiV1PoolEventsResponse200,
        PostApiV1PoolEventsResponse401,
        PostApiV1PoolEventsResponse404,
        PostApiV1PoolEventsResponse422,
    ]
]:
    """Creates a pool event

     This endpoint facilitates the creation of pool events and allows for the aggregation of stocks based
    on selected logic.

    It supports three methods for pooling:
    1. **Fixed Amount Pooling**: Using the `createFixedSamplePoolingEvent` schema, which draws a fixed
    amount from all listed stocks.

    2. **Custom Amount Pooling**: Using the `createCustomSamplePoolingEvent` schema, which allows for
    drawing custom amounts from each stock.
    3. **Total Consumption Pooling**: Using the `createCustomSamplePoolingEvent` schema, which draws and
    consumes the entire amount from each stock.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['CreateConsumeSamplePoolingEvent', 'CreateCustomSamplePoolingEvent',
            'CreateFixedSamplePoolingEvent']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiV1PoolEventsResponse200, PostApiV1PoolEventsResponse401, PostApiV1PoolEventsResponse404, PostApiV1PoolEventsResponse422]]
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
    body: Union["CreateConsumeSamplePoolingEvent", "CreateCustomSamplePoolingEvent", "CreateFixedSamplePoolingEvent"],
) -> Optional[
    Union[
        PostApiV1PoolEventsResponse200,
        PostApiV1PoolEventsResponse401,
        PostApiV1PoolEventsResponse404,
        PostApiV1PoolEventsResponse422,
    ]
]:
    """Creates a pool event

     This endpoint facilitates the creation of pool events and allows for the aggregation of stocks based
    on selected logic.

    It supports three methods for pooling:
    1. **Fixed Amount Pooling**: Using the `createFixedSamplePoolingEvent` schema, which draws a fixed
    amount from all listed stocks.

    2. **Custom Amount Pooling**: Using the `createCustomSamplePoolingEvent` schema, which allows for
    drawing custom amounts from each stock.
    3. **Total Consumption Pooling**: Using the `createCustomSamplePoolingEvent` schema, which draws and
    consumes the entire amount from each stock.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['CreateConsumeSamplePoolingEvent', 'CreateCustomSamplePoolingEvent',
            'CreateFixedSamplePoolingEvent']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiV1PoolEventsResponse200, PostApiV1PoolEventsResponse401, PostApiV1PoolEventsResponse404, PostApiV1PoolEventsResponse422]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["CreateConsumeSamplePoolingEvent", "CreateCustomSamplePoolingEvent", "CreateFixedSamplePoolingEvent"],
) -> Response[
    Union[
        PostApiV1PoolEventsResponse200,
        PostApiV1PoolEventsResponse401,
        PostApiV1PoolEventsResponse404,
        PostApiV1PoolEventsResponse422,
    ]
]:
    """Creates a pool event

     This endpoint facilitates the creation of pool events and allows for the aggregation of stocks based
    on selected logic.

    It supports three methods for pooling:
    1. **Fixed Amount Pooling**: Using the `createFixedSamplePoolingEvent` schema, which draws a fixed
    amount from all listed stocks.

    2. **Custom Amount Pooling**: Using the `createCustomSamplePoolingEvent` schema, which allows for
    drawing custom amounts from each stock.
    3. **Total Consumption Pooling**: Using the `createCustomSamplePoolingEvent` schema, which draws and
    consumes the entire amount from each stock.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['CreateConsumeSamplePoolingEvent', 'CreateCustomSamplePoolingEvent',
            'CreateFixedSamplePoolingEvent']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiV1PoolEventsResponse200, PostApiV1PoolEventsResponse401, PostApiV1PoolEventsResponse404, PostApiV1PoolEventsResponse422]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["CreateConsumeSamplePoolingEvent", "CreateCustomSamplePoolingEvent", "CreateFixedSamplePoolingEvent"],
) -> Optional[
    Union[
        PostApiV1PoolEventsResponse200,
        PostApiV1PoolEventsResponse401,
        PostApiV1PoolEventsResponse404,
        PostApiV1PoolEventsResponse422,
    ]
]:
    """Creates a pool event

     This endpoint facilitates the creation of pool events and allows for the aggregation of stocks based
    on selected logic.

    It supports three methods for pooling:
    1. **Fixed Amount Pooling**: Using the `createFixedSamplePoolingEvent` schema, which draws a fixed
    amount from all listed stocks.

    2. **Custom Amount Pooling**: Using the `createCustomSamplePoolingEvent` schema, which allows for
    drawing custom amounts from each stock.
    3. **Total Consumption Pooling**: Using the `createCustomSamplePoolingEvent` schema, which draws and
    consumes the entire amount from each stock.

    Ensure the request body matches the structure defined in the referenced schemas for successful
    operation.

    Args:
        body (Union['CreateConsumeSamplePoolingEvent', 'CreateCustomSamplePoolingEvent',
            'CreateFixedSamplePoolingEvent']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiV1PoolEventsResponse200, PostApiV1PoolEventsResponse401, PostApiV1PoolEventsResponse404, PostApiV1PoolEventsResponse422]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
