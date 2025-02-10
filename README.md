# labguru-api-client

Python api client for accessing the Labguru Electronic Lab Notebook.

This package contains two main groups of code:

1. Generated code from the OpenAPI spec for the Labguru API, using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). This code is in the `labguru_api_client` directory.
1. Wrapper functions around the generated code to make it easier to use. This part is still in development.

## Installing

You can install this package using pip:

```python
pip install labguru-api-client
```

## Usage (wrapper functions)

Wrapper functions are under active development and are expected to change. For now, a few experiment-related fucntions have been defined.

```python
from labguru_wrapper.labguru_api import LabguruAPI

# define env vars in ~/.labguru.env
# LABGURU_API_KEY is required
# LABGURU_BASE_URL is optional
labguru = LabguruAPI()

exp1_1 = labguru.get_experiment(1)
# returned object will be a dict/json representation of the experiment
print(exp1_1["title"])

exp1_updated = labguru.update_experiment(1, {"title": "Modified title"})
assert labguru.get_experiment(1)["title"] == "Modified_title"
```

## Usage (generated code)

Create a client and make an example request to get an experiment by id. Your Labguru API key should be stored in an environment variable called `LABGURU_API_KEY`. Extracing information from the response can be done by parsing the `response.content` attribute. The Labguru openAPI spec did not include a response model for their endpoints, so `response.parsed` will be `None`.

```python
import json
from labguru_api_client import Client
from labguru_api_client.api.experiments import get_api_v1_experiments_id

client = Client(base_url="https://my.labguru.com/")
exp_1 = get_api_v1_experiments_id.sync_detailed(client=client, token=os.getenv("LABGURU_API_KEY"), id=1)
if exp_1.status_code == 200:
    print(json.loads(exp_1.content)["title"])
```

To update or create an experiment, use the generated models to create a body for the request.

```python
import json
from labguru_api_client import Client
from labguru_api_client.api.experiments import put_api_v1_experiments_id
from labguru_api_client.models import UpdateExperimentItem, UpdateExperiment

updated_experiment_item = UpdateExperimentItem.from_dict({
    "title": "My new title"
})
updated_experiment = UpdateExperiment(token=os.getenv("LABGURU_API_KEY"), item=updated_experiment_item)

exp_1_put = put_api_v1_experiments_id.sync_detailed(client=client, id=1, body=updated_experiment)
exp_1_updated = get_api_v1_experiments_id.sync_detailed(client=client, token=os.getenv("LABGURU_API_KEY"), id=1)
if exp_1_put.status_code == 200 and exp_1_updated.status_code == 200:
    assert json.loads(exp_1_updated.content)["title"] == "My new title"
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `labguru_api_client.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from labguru_api_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://my.labguru.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from labguru_api_client import Client

client = Client(
    base_url="https://my.labguru.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://my.labguru.com", proxies="http://localhost:8030"))
```
