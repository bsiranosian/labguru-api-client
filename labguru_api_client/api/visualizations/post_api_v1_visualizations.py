from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_visualization import AddVisualization
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    *,
    body: AddVisualization,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/visualizations",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Unauthorized]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 401:
        response_401 = Unauthorized.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddVisualization,
) -> Response[Union[Any, Unauthorized]]:
    """add visualization

     This endpoint creates a visualization.

    To add visualization to a dataset, provide a name, the dataset ID it corresponds to, and an
    attachment ID (the ID of the visualization file uploaded to Labguru).
    Once added, the visualization will appear under the 'Visualizations' tab of a dataset.

    For a detailed guide on creating dataset visualizations, including a step-by-step process and
    practical examples, refer to our comprehensive article: [How To Create Dataset
    Visualization](https://help.labguru.com/en/articles/8741020-how-to-create-dataset-visualization).

    Args:
        body (AddVisualization):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Unauthorized]]
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
    body: AddVisualization,
) -> Optional[Union[Any, Unauthorized]]:
    """add visualization

     This endpoint creates a visualization.

    To add visualization to a dataset, provide a name, the dataset ID it corresponds to, and an
    attachment ID (the ID of the visualization file uploaded to Labguru).
    Once added, the visualization will appear under the 'Visualizations' tab of a dataset.

    For a detailed guide on creating dataset visualizations, including a step-by-step process and
    practical examples, refer to our comprehensive article: [How To Create Dataset
    Visualization](https://help.labguru.com/en/articles/8741020-how-to-create-dataset-visualization).

    Args:
        body (AddVisualization):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Unauthorized]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddVisualization,
) -> Response[Union[Any, Unauthorized]]:
    """add visualization

     This endpoint creates a visualization.

    To add visualization to a dataset, provide a name, the dataset ID it corresponds to, and an
    attachment ID (the ID of the visualization file uploaded to Labguru).
    Once added, the visualization will appear under the 'Visualizations' tab of a dataset.

    For a detailed guide on creating dataset visualizations, including a step-by-step process and
    practical examples, refer to our comprehensive article: [How To Create Dataset
    Visualization](https://help.labguru.com/en/articles/8741020-how-to-create-dataset-visualization).

    Args:
        body (AddVisualization):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Unauthorized]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddVisualization,
) -> Optional[Union[Any, Unauthorized]]:
    """add visualization

     This endpoint creates a visualization.

    To add visualization to a dataset, provide a name, the dataset ID it corresponds to, and an
    attachment ID (the ID of the visualization file uploaded to Labguru).
    Once added, the visualization will appear under the 'Visualizations' tab of a dataset.

    For a detailed guide on creating dataset visualizations, including a step-by-step process and
    practical examples, refer to our comprehensive article: [How To Create Dataset
    Visualization](https://help.labguru.com/en/articles/8741020-how-to-create-dataset-visualization).

    Args:
        body (AddVisualization):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
