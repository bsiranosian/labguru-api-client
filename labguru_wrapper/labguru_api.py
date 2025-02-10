import os
import json
from labguru_api_client import AuthenticatedClient
from labguru_api_client.api.experiments import (
    get_api_v1_experiments,
    get_api_v1_experiments_id,
    put_api_v1_experiments_id,
    post_api_v1_experiments,
)
from labguru_api_client.models import UpdateExperiment, UpdateExperimentItem
from dotenv import load_dotenv
from typing import Optional

# Your LabguruAPI and ExperimentsAPI classes go here...
class LabguruAPI:
    """
    A wrapper for labguru-api-client.
    
    Loads configuration, handles authentication, and provides high-level methods
    to access various endpoints.
    """
    def __init__(self, env_file: Optional[str] = None):
        if env_file is None:
            env_file = os.path.expanduser("~/.labguru.env")
        self._load_env(env_file)
        self.token = os.getenv("LABGURU_API_KEY")
        if not self.token:
            raise ValueError("LABGURU_API_KEY not found in environment.")
        self.base_url = os.getenv("LABGURU_BASE_URL", "https://my.labguru.com")
        self.client = AuthenticatedClient(base_url=self.base_url, token=self.token)
        self.experiments = ExperimentsAPI(self.client, self.token)

    def _load_env(self, env_file: str) -> None:
        if os.path.exists(env_file):
            load_dotenv(dotenv_path=env_file)
            # ensure required variables are set
            if not os.getenv("LABGURU_API_KEY"):
                raise ValueError("LABGURU_API_KEY not found in environment.")
        else:
            raise FileNotFoundError(f"Environment file {env_file} not found. Please create it with at least LABGURU_API_KEY defined.")

    # High-level methods that delegate to ExperimentsAPI:
    def get_all_experiments(self, page: int = 1, meta: str = "false"):
        return self.experiments.get_all(page=page, meta=meta)

    def get_experiment(self, experiment_id: int):
        return self.experiments.get(experiment_id)

    def update_experiment(self, experiment_id: int, update_fields: dict):
        return self.experiments.update(experiment_id, update_fields)

    def create_experiment(self, experiment_data: dict):
        return self.experiments.create(experiment_data)



class ExperimentsAPI:
    """
    A dedicated class for experiment-related endpoints.
    
    Provides methods:
        - get_all(page, meta)
        - get(experiment_id)
        - update(experiment_id, update_fields)
        - create(experiment_data)
    """

    def __init__(self, client: AuthenticatedClient, token: str):
        self.client = client
        self.token = token

    def get_all(self, page: int = 1, meta: str = "false"):
        response = get_api_v1_experiments.sync_detailed(
            client=self.client, token=self.token, page=page, meta=meta
        )
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error retrieving experiments: {response.status_code} - {response.content}"
            )

    def get(self, experiment_id: int):
        response = get_api_v1_experiments_id.sync_detailed(
            client=self.client, token=self.token, id=experiment_id
        )
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error retrieving experiment {experiment_id}: {response.status_code} - {response.content}"
            )

    def update(self, experiment_id: int, update_fields: dict):
        """
        Update an experiment.
        
        :param experiment_id: The ID of the experiment to update.
        :param update_fields: Dictionary with the fields to update (e.g. {"title": "NEW TITLE"}).
        """
        # Create an UpdateExperimentItem from the dictionary.
        update_experiment_item = UpdateExperimentItem.from_dict(update_fields)
        # Wrap it in the parent model, providing the token.
        updated_experiment_payload = UpdateExperiment(
            token=self.token, item=update_experiment_item
        )
        response = put_api_v1_experiments_id.sync_detailed(
            client=self.client, id=experiment_id, body=updated_experiment_payload
        )
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error updating experiment {experiment_id}: {response.status_code} - {response.content}"
            )

    def create(self, experiment_data: dict):
        """
        Create a new experiment.
        
        :param experiment_data: Dictionary with experiment fields.
        """
        # Assuming your API spec defines a CreateExperiment model similar to UpdateExperiment,
        # the generated client might have models like CreateExperiment and CreateExperimentItem.
        from labguru_api_client.models import CreateExperiment, CreateExperimentItem

        create_experiment_item = CreateExperimentItem.from_dict(experiment_data)
        create_experiment_payload = CreateExperiment(
            token=self.token, item=create_experiment_item
        )
        response = post_api_v1_experiments.sync_detailed(
            client=self.client, body=create_experiment_payload
        )
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error creating experiment: {response.status_code} - {response.content}"
            )
