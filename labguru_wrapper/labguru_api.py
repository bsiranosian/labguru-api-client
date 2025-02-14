import os
import json
import requests
from pathlib import Path
from labguru_api_client import AuthenticatedClient

# Experiments endpoints
from labguru_api_client.api.experiments import (
    get_api_v1_experiments,
    get_api_v1_experiments_id,
    put_api_v1_experiments_id,
    post_api_v1_experiments,
)

# Folders (Milestones) endpoints
from labguru_api_client.api.folders import (
    post_api_v1_milestones,
    get_api_v1_milestones,
    put_api_v1_milestones_id,
    get_api_v1_milestones_id,
)

# Projects endpoints
from labguru_api_client.api.projects import (
    post_api_v1_projects,
    get_api_v1_projects,
    put_api_v1_projects_id,
    get_api_v1_projects_id,
)

# Attachments endpoints
from labguru_api_client.api.attachments import (
    post_api_v1_attachments,
    put_api_v1_attachments_id,
    get_api_v1_attachments_id,
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
        self.folders = FoldersAPI(self.client, self.token)
        self.projects = ProjectsAPI(self.client, self.token)
        self.attachments = AttachmentsAPI(self.client, self.token)

    def _load_env(self, env_file: str) -> None:
        if os.path.exists(env_file):
            load_dotenv(dotenv_path=env_file)
            # ensure required variables are set
            if not os.getenv("LABGURU_API_KEY"):
                raise ValueError("LABGURU_API_KEY not found in environment.")
        else:
            raise FileNotFoundError(f"Environment file {env_file} not found. Please create it with at least LABGURU_API_KEY defined.")

    # -- Experiment methods --
    def get_all_experiments(self, page: int = 1, meta: str = "false"):
        return self.experiments.get_all(page=page, meta=meta)

    def get_experiment(self, experiment_id: int):
        return self.experiments.get(experiment_id)

    def update_experiment(self, experiment_id: int, update_fields: dict):
        return self.experiments.update(experiment_id, update_fields)

    def create_experiment(self, experiment_data: dict):
        return self.experiments.create(experiment_data)

    def delete_experiment(self, experiment_id: int):
        return self.experiments.delete(experiment_id)

    # -- Folders (Milestones) methods --
    def get_all_folders(
        self,
        page: int = 1,
        meta: str = "false",
        period: Optional[str] = None,
        project_id: Optional[str] = None,
    ):
        return self.folders.get_all(page=page, meta=meta, period=period, project_id=project_id)

    def get_folder(self, folder_id: int):
        return self.folders.get(folder_id)

    def update_folder(self, folder_id: int, update_fields: dict):
        return self.folders.update(folder_id, update_fields)

    def create_folder(self, folder_data: dict):
        return self.folders.create(folder_data)

    def delete_folder(self, folder_id: int):
        return self.folders.delete(folder_id)

    # -- Projects methods --
    def get_all_projects(self, page: int = 1, meta: str = "false"):
        return self.projects.get_all(page=page, meta=meta)

    def get_project(self, project_id: int):
        return self.projects.get(project_id)

    def update_project(self, project_id: int, update_fields: dict):
        return self.projects.update(project_id, update_fields)

    def create_project(self, project_data: dict):
        return self.projects.create(project_data)

    def delete_project(self, project_id: int):
        return self.projects.delete(project_id)

    # -- Attachments methods --
    def upload_attachment(self, file_path: Path | str, attach_to_uuid: str = None, description: str = None):
        return self.attachments.upload(file_path, attach_to_uuid, description)

    def get_attachment(self, attachment_id: int):
        return self.attachments.get(attachment_id)

    def update_attachment(self, attachment_id: int, update_fields: dict):
        return self.attachments.update(attachment_id, update_fields)

    def delete_attachment(self, attachment_id: int):
        return self.attachments.delete(attachment_id)


class ExperimentsAPI:
    """
    A dedicated class for experiment-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(experiment_id)
        - update(experiment_id, update_fields)
        - create(experiment_data)
        - delete(experiment_id)
    """

    def __init__(self, client: AuthenticatedClient, token: str):
        self.client = client
        self.token = token

    def get_all(self, page: int = 1, meta: str = "false"):
        response = get_api_v1_experiments.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving experiments: {response.status_code} - {json.loads(response.content)}")

    def get(self, experiment_id: int):
        response = get_api_v1_experiments_id.sync_detailed(client=self.client, token=self.token, id=experiment_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving experiment {experiment_id}: {response.status_code} - {json.loads(response.content)}")

    def update(self, experiment_id: int, update_fields: dict):
        """
        Update an experiment.

        :param experiment_id: The ID of the experiment to update.
        :param update_fields: Dictionary with the fields to update (e.g. {"title": "NEW TITLE"}).
        """
        # Create an UpdateExperimentItem from the dictionary.
        update_experiment_item = UpdateExperimentItem.from_dict(update_fields)
        # Wrap it in the parent model, providing the token.
        updated_experiment_payload = UpdateExperiment(token=self.token, item=update_experiment_item)  # type: ignore
        response = put_api_v1_experiments_id.sync_detailed(client=self.client, id=experiment_id, body=updated_experiment_payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating experiment {experiment_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, experiment_data: dict):
        """
        Create a new experiment.

        :param experiment_data: Dictionary with experiment fields.
        """
        from labguru_api_client.models import AddExperiment, AddExperimentItem

        create_experiment_item = AddExperimentItem.from_dict(experiment_data)
        create_experiment_payload = AddExperiment(token=self.token, item=create_experiment_item)  # type: ignore
        response = post_api_v1_experiments.sync_detailed(client=self.client, body=create_experiment_payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating experiment: {response.status_code} - {json.loads(response.content)}")

    def delete(self, experiment_id: int):
        """
        Delete an experiment. Not in the openAPI spec, so we use requests directly.

        :param experiment_id: The ID of the experiment to delete.
        """
        base_url = os.getenv("LABGURU_BASE_URL", "https://my.labguru.com")
        response = requests.delete(f"{base_url}/api/v1/experiments/{experiment_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting experiment {experiment_id}: {response.status_code} - {response.content}")


class FoldersAPI:
    """
    A dedicated class for folder (milestone) related endpoints.

    Provides methods:
      - get_all(page, meta, period, project_id)
      - get(folder_id)
      - update(folder_id, update_fields)
      - create(folder_data)
      - delete(folder_id)
    """

    def __init__(self, client: AuthenticatedClient, token: str):
        self.client = client
        self.token = token

    def get_all(self, page: int = 1, meta: str = "false", period: Optional[str] = None, project_id: Optional[str] = None):
        params = {"token": self.token, "page": page, "meta": meta}
        if period:
            params["period"] = period
        if project_id:
            params["project_id"] = project_id
        response = get_api_v1_milestones.sync_detailed(client=self.client, **params)  # type: ignore
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving folders: {response.status_code} - {json.loads(response.content)}")

    def get(self, folder_id: int):
        response = get_api_v1_milestones_id.sync_detailed(client=self.client, token=self.token, id=folder_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving folder {folder_id}: {response.status_code} - {json.loads(response.content)}")

    def update(self, folder_id: int, update_fields: dict):
        from labguru_api_client.models import UpdateFolder, UpdateFolderItem

        update_folder_item = UpdateFolderItem.from_dict(update_fields)
        update_folder_payload = UpdateFolder(token=self.token, item=update_folder_item)  # type: ignore
        response = put_api_v1_milestones_id.sync_detailed(client=self.client, id=folder_id, body=update_folder_payload)
        if response.status_code != 200:
            raise Exception(f"Error updating folder {folder_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, folder_data: dict):
        from labguru_api_client.models import CreateFolder, CreateFolderItem

        folder_item = CreateFolderItem.from_dict(folder_data)
        folder_payload = CreateFolder(token=self.token, item=folder_item)  # type: ignore
        response = post_api_v1_milestones.sync_detailed(client=self.client, body=folder_payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating folder: {response.status_code} - {json.loads(response.content)}")

    def delete(self, folder_id: int):
        base_url = os.getenv("LABGURU_BASE_URL", "https://my.labguru.com")
        response = requests.delete(f"{base_url}/api/v1/milestones/{folder_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting folder {folder_id}: {response.status_code} - {response.content}")


class ProjectsAPI:
    """
    A dedicated class for project-related endpoints.

    Provides methods:
      - get_all(page, meta)
      - get(project_id)
      - update(project_id, update_fields)
      - create(project_data)
      - delete(project_id)
    """

    def __init__(self, client: AuthenticatedClient, token: str):
        self.client = client
        self.token = token

    def get_all(self, page: int = 1, meta: str = "false"):
        response = get_api_v1_projects.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving projects: {response.status_code} - {json.loads(response.content)}")

    def get(self, project_id: int):
        response = get_api_v1_projects_id.sync_detailed(client=self.client, token=self.token, id=project_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving project {project_id}: {response.status_code} - {json.loads(response.content)}")

    def update(self, project_id: int, update_fields: dict):
        from labguru_api_client.models import UpdateProject, UpdateProjectItem

        update_project_item = UpdateProjectItem.from_dict(update_fields)
        update_project_payload = UpdateProject(token=self.token, item=update_project_item)  # type: ignore
        response = put_api_v1_projects_id.sync_detailed(client=self.client, id=project_id, body=update_project_payload)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating project {project_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, project_data: dict):
        from labguru_api_client.models import CreateProject, CreateProjectItem

        project_item = CreateProjectItem.from_dict(project_data)
        project_payload = CreateProject(token=self.token, item=project_item)  # type: ignore
        response = post_api_v1_projects.sync_detailed(client=self.client, body=project_payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating project: {response.status_code} - {json.loads(response.content)}")

    def delete(self, project_id: int):
        raise NotImplementedError("Delete project is not supported by the Labguru API.")
        base_url = os.getenv("LABGURU_BASE_URL", "https://my.labguru.com")
        response = requests.delete(f"{base_url}/api/v1/projects/{project_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting project {project_id}: {response.status_code} - {response.content}")


class AttachmentsAPI:
    """
    A dedicated class for attachment-related endpoints.

    Provides methods:
      - upload(attachment_data, files)
      - get(attachment_id)
      - update(attachment_id, update_fields)
      - delete(attachment_id)
    """

    def __init__(self, client: AuthenticatedClient, token: str):
        self.client = client
        self.token = token

    def upload(self, file_path: Path | str, attach_to_uuid: str = None, description: str = None):
        """
        Upload a file attachment.

        :param attachment_data: Dictionary of form fields for the attachment.
        :param files: Dictionary of file objects to upload.
        """
        from labguru_api_client.models import CreateAttachment
        from labguru_api_client.types import File

        with open(file_path, "rb") as file:
            title = Path(file_path).name
            itemattachment = File(payload=file, file_name=title)
            attachment_payload = CreateAttachment(
                token=self.token,
                itemattachment=itemattachment,
                itemattach_to_uuid=attach_to_uuid,
                itemtitle=title,
                itemdescription=description,
            )  # type: ignore
            response = post_api_v1_attachments.sync_detailed(client=self.client, body=attachment_payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error uploading attachment: {response.status_code} - {json.loads(response.content)}")

    def get(self, attachment_id: int):
        response = get_api_v1_attachments_id.sync_detailed(client=self.client, token=self.token, id=attachment_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving attachment {attachment_id}: {response.status_code} - {json.loads(response.content)}")

    def update(self, attachment_id: int, update_fields: dict):
        from labguru_api_client.models import UpdateAttachment, UpdateAttachmentItem

        update_attachment_item = UpdateAttachmentItem.from_dict(update_fields)
        update_payload = UpdateAttachment(token=self.token, item=update_attachment_item)  # type: ignore
        response = put_api_v1_attachments_id.sync_detailed(client=self.client, id=attachment_id, body=update_payload)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating attachment {attachment_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, attachment_id: int):
        base_url = os.getenv("LABGURU_BASE_URL", "https://my.labguru.com")
        response = requests.delete(f"{base_url}/api/v1/attachments/{attachment_id}?token={self.token}")
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Error deleting attachment {attachment_id}: {response.status_code} - {response.content}")
