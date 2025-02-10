from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.not_found import NotFound
from ...models.post_api_v1_measurements_body import PostApiV1MeasurementsBody
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiV1MeasurementsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/measurements",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NotFound, Unauthorized]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 401:
        response_401 = Unauthorized.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NotFound, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiV1MeasurementsBody,
) -> Response[Union[Any, NotFound, Unauthorized]]:
    """Add measurements

     This endpoint allows the submission of measurement data from connected equipment to a specific
    experiment,

    It accepts a measurement value and populates it into a designated form input field.

    For more information and a detailed example of how to use the ‘Measurement’ endpoint, refer to our
    article on [How to capture data from instruments using the 'measurement' API
    endpoint](https://help.labguru.com/en/articles/10300263-how-to-capture-data-from-instruments-using-
    the-measurement-api-endpoint)


    Args:
        body (PostApiV1MeasurementsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFound, Unauthorized]]
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
    body: PostApiV1MeasurementsBody,
) -> Optional[Union[Any, NotFound, Unauthorized]]:
    """Add measurements

     This endpoint allows the submission of measurement data from connected equipment to a specific
    experiment,

    It accepts a measurement value and populates it into a designated form input field.

    For more information and a detailed example of how to use the ‘Measurement’ endpoint, refer to our
    article on [How to capture data from instruments using the 'measurement' API
    endpoint](https://help.labguru.com/en/articles/10300263-how-to-capture-data-from-instruments-using-
    the-measurement-api-endpoint)


    Args:
        body (PostApiV1MeasurementsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFound, Unauthorized]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiV1MeasurementsBody,
) -> Response[Union[Any, NotFound, Unauthorized]]:
    """Add measurements

     This endpoint allows the submission of measurement data from connected equipment to a specific
    experiment,

    It accepts a measurement value and populates it into a designated form input field.

    For more information and a detailed example of how to use the ‘Measurement’ endpoint, refer to our
    article on [How to capture data from instruments using the 'measurement' API
    endpoint](https://help.labguru.com/en/articles/10300263-how-to-capture-data-from-instruments-using-
    the-measurement-api-endpoint)


    Args:
        body (PostApiV1MeasurementsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFound, Unauthorized]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiV1MeasurementsBody,
) -> Optional[Union[Any, NotFound, Unauthorized]]:
    """Add measurements

     This endpoint allows the submission of measurement data from connected equipment to a specific
    experiment,

    It accepts a measurement value and populates it into a designated form input field.

    For more information and a detailed example of how to use the ‘Measurement’ endpoint, refer to our
    article on [How to capture data from instruments using the 'measurement' API
    endpoint](https://help.labguru.com/en/articles/10300263-how-to-capture-data-from-instruments-using-
    the-measurement-api-endpoint)


    Args:
        body (PostApiV1MeasurementsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFound, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
