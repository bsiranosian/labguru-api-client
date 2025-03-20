import os
import json
import requests
from pathlib import Path
from labguru_api_client import AuthenticatedClient
import pandas as pd

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

# Biocollections (generic items) endpoints
from labguru_api_client.api.generic_items import (
    post_api_v1_biocollections_generic_collection_name,
    get_api_v1_biocollections_generic_collection_name,
    put_api_v1_biocollections_generic_collection_name_id,
    get_api_v1_biocollections_generic_collection_name_id,
)

# Plasmids endpoints
from labguru_api_client.api.plasmids import (
    post_api_v1_plasmids,
    get_api_v1_plasmids,
    put_api_v1_plasmids_id,
    get_api_v1_plasmids_id,
)

# Protocols endpoints
from labguru_api_client.api.protocols import (
    get_api_v1_protocols,
    get_api_v1_protocols_id,
    post_api_v1_protocols,
    put_api_v1_protocols_id,
)

# SOPs endpoints
from labguru_api_client.api.so_ps import (
    get_api_v1_sops,
    get_api_v1_sops_id,
    post_api_v1_sops,
    put_api_v1_sops_id,
)

# Antibodies endpoints
from labguru_api_client.api.antibodies import (
    get_api_v1_antibodies,
    get_api_v1_antibodies_id,
    post_api_v1_antibodies,
    put_api_v1_antibodies_id,
)

# Cell lines endpoints
from labguru_api_client.api.cell_lines import (
    get_api_v1_cell_lines,
    get_api_v1_cell_lines_id,
    post_api_v1_cell_lines,
    put_api_v1_cell_lines_id,
)

# Consumables endpoints
from labguru_api_client.api.consumables import (
    get_api_v1_materials,
    get_api_v1_materials_id,
    post_api_v1_materials,
    put_api_v1_materials_id,
)

# Primers endpoints
from labguru_api_client.api.primers import (
    get_api_v1_primers,
    get_api_v1_primers_id,
    post_api_v1_primers,
    put_api_v1_primers_id,
)

# Plates endpoints
from labguru_api_client.api.plates import (
    get_api_v1_plates,
    get_api_v1_plates_id,
)

# Stocks endpoints
from labguru_api_client.api.stocks import (
    get_api_v1_stocks,
    get_api_v1_stocks_id,
    post_api_v1_stocks,
    put_api_v1_stocks_id,
)

# Storage endpoints
from labguru_api_client.api.storages import (
    get_api_v1_storages,
    get_api_v1_storages_id,
    post_api_v1_storages,
    put_api_v1_storages_id,
)

# Sequences endpoints
from labguru_api_client.api.sequences import (
    get_api_v1_sequences,
    get_api_v1_sequences_id,
    post_api_v1_sequences,
    put_api_v1_sequences_id,
)

# Proteins endpoints
from labguru_api_client.api.proteins import (
    get_api_v1_proteins,
    get_api_v1_proteins_id,
    post_api_v1_proteins,
    put_api_v1_proteins_id,
)

# Equipment endpoints
from labguru_api_client.api.equipment import (
    get_api_v1_instruments,
    get_api_v1_instruments_id,
    post_api_v1_instruments,
    put_api_v1_instruments_id,
)

# Datasets endpoints
from labguru_api_client.api.datasets import get_api_v1_datasets, get_api_v1_datasets_id, post_api_v1_datasets

# Boxes endpoints
from labguru_api_client.api.boxes import (
    get_api_v1_boxes,
    get_api_v1_boxes_id,
    post_api_v1_boxes,
    put_api_v1_boxes_id,
)


# Biocollections (filters) endpoints
from labguru_api_client.api.filters import get_api_v1_biocollections_collection_name

# Models for experiments
from labguru_api_client.models import UpdateExperiment, UpdateExperimentItem, AddExperiment, AddExperimentItem

# Models for generic biocollections items
from labguru_api_client.models import (
    CreateGenericItem,
    CreateGenericItemItem,
    UpdateGenericItem,
    UpdateGenericItemItem,
)

# Models for plasmids
from labguru_api_client.models import CreatePlasmid, CreatePlasmidItem, UpdatePlasmid, UpdatePlasmidItem

# Models for protocols
from labguru_api_client.models import CreateProtocol, UpdateProtocol, UpdateProtocolItem

# Models for SOPs
from labguru_api_client.models import CreateSOP, CreateSOPItem, UpdateSOP, UpdateSOPItem

# Models for antibodies
from labguru_api_client.models import CreateAntibody, CreateAntibodyItem, UpdateAntibody, UpdateAntibodyItem

# Models for cell lines
from labguru_api_client.models import CreateCellLine, CreateCellLineItem, UpdateCellLine, UpdateCellLineItem

# Models for consumables
from labguru_api_client.models import CreateMaterial, CreateMaterialItem, UpdateMaterial, UpdateMaterialItem

# Models for primers
from labguru_api_client.models import CreatePrimer, CreatePrimerItem, UpdatePrimer, UpdatePrimerItem

# Models for plates (don't exist)

# Models for stocks
from labguru_api_client.models import CreateStock, CreateStockItem, UpdateStock, UpdateStockItem

# Models for storage
from labguru_api_client.models import CreateStorage, CreateStorageItem, UpdateStorage, UpdateStorageItem

# Models for sequences
from labguru_api_client.models import CreateSequence, CreateSequenceItem, UpdateSequence, UpdateSequenceItem

# Models for proteins
from labguru_api_client.models import CreateProtein, CreateProteinItem, UpdateProtein, UpdateProteinItem

# Models for equipment (don't exist)
# Models for datasets
from labguru_api_client.models import CreateDataset, CreateDatasetItem

# Models for boxes
from labguru_api_client.models import CreateBox, CreateBoxItem, UpdateBox, UpdateBoxItem


from labguru_api_client.types import Unset, UNSET
from dotenv import load_dotenv
from typing import Optional


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
        self.experiments = ExperimentsAPI(self.client, self.token, self.base_url)
        self.folders = FoldersAPI(self.client, self.token, self.base_url)
        self.projects = ProjectsAPI(self.client, self.token, self.base_url)
        self.attachments = AttachmentsAPI(self.client, self.token, self.base_url)
        self.biocollections = BiocollectionsAPI(self.client, self.token, self.base_url)
        self.plasmids = PlasmidsAPI(self.client, self.token, self.base_url)
        self.protocols = ProtocolsAPI(self.client, self.token, self.base_url)
        self.sops = SopsAPI(self.client, self.token, self.base_url)
        self.antibodies = AntibodiesAPI(self.client, self.token, self.base_url)
        self.cell_lines = CellLinesAPI(self.client, self.token, self.base_url)
        self.consumables = ConsumablesAPI(self.client, self.token, self.base_url)
        self.primers = PrimersAPI(self.client, self.token, self.base_url)
        self.plates = PlatesAPI(self.client, self.token, self.base_url)
        self.stocks = StocksAPI(self.client, self.token, self.base_url)
        self.storages = StoragesAPI(self.client, self.token, self.base_url)
        self.sequences = SequencesAPI(self.client, self.token, self.base_url)
        self.proteins = ProteinsAPI(self.client, self.token, self.base_url)
        self.equipment = EquipmentAPI(self.client, self.token, self.base_url)
        self.datasets = DatasetsAPI(self.client, self.token, self.base_url)
        self.boxes = BoxesAPI(self.client, self.token, self.base_url)

    def _load_env(self, env_file: str) -> None:
        if os.path.exists(env_file):
            load_dotenv(dotenv_path=env_file)
            # ensure required variables are set
            if not os.getenv("LABGURU_API_KEY"):
                raise ValueError("LABGURU_API_KEY not found in environment.")
        else:
            raise FileNotFoundError(f"Environment file {env_file} not found. Please create it with at least LABGURU_API_KEY defined.")

    def _get_list_all_pages(self, get_fun):
        current_page = 1
        get_more_pages = True
        data_list = []
        while get_more_pages:
            data_current_page = get_fun(page=current_page, meta=True)
            data_list.extend(data_current_page["data"])
            if data_current_page["meta"]["page_count"] > current_page:
                current_page += 1
            else:
                get_more_pages = False
        return data_list

    # -- Experiment methods --
    def get_experiments_all(self):
        return self._get_list_all_pages(self.experiments.get_all)

    def get_experiment_by_id(self, id: int):
        return self.experiments.get(id)

    def update_experiment(self, id: int, update_fields: dict):
        return self.experiments.update(id, update_fields)

    def create_experiment(self, experiment_data: dict):
        return self.experiments.create(experiment_data)

    def delete_experiment(self, id: int):
        return self.experiments.delete(id)

    # -- Folders (Milestones) methods --
    def get_folders_all(self):
        return self._get_list_all_pages(self.folders.get_all)

    def get_folder_by_id(self, id: int):
        return self.folders.get(id)

    def update_folder(self, id: int, update_fields: dict):
        return self.folders.update(id, update_fields)

    def create_folder(self, folder_data: dict):
        return self.folders.create(folder_data)

    def delete_folder(self, id: int):
        return self.folders.delete(id)

    # -- Projects methods --
    def get_projects_all(self):
        return self._get_list_all_pages(self.projects.get_all)

    def get_project_by_id(self, id: int):
        return self.projects.get(id)

    def update_project(self, id: int, update_fields: dict):
        return self.projects.update(id, update_fields)

    def create_project(self, project_data: dict):
        return self.projects.create(project_data)

    def delete_project(self, id: int):
        return self.projects.delete(id)

    # -- Attachments methods --
    def upload_attachment(self, file_path: Path | str, attach_to_uuid: str | None | Unset = None, description: str | None | Unset = None):
        if attach_to_uuid is None:
            attach_to_uuid = UNSET
        if description is None:
            description = UNSET
        return self.attachments.upload(file_path, attach_to_uuid, description)

    def get_attachments_all(self):
        return self._get_list_all_pages(self.attachments.get_all)

    def get_attachment_by_id(self, id: int):
        return self.attachments.get(id)

    def update_attachment(self, id: int, update_fields: dict):
        return self.attachments.update(id, update_fields)

    def delete_attachment(self, id: int):
        return self.attachments.delete(id)

    # -- Biocollections methods --
    def filter_biocollection_items(
        self,
        collection_name: str,
        filter_field: str,
        filter_operator: str,
        filter_value: str,
        page: int = 1,
        meta: str = "true",
        kendo: str = "true",
        filter_logic: str = "and",
    ):
        return self.biocollections.filter_items(
            collection_name, filter_field, filter_operator, filter_value, page, meta, kendo, filter_logic
        )

    def get_generic_items_all(self, generic_collection_name: str):
        return self._get_list_all_pages(self.biocollections.get_generic_items(generic_collection_name))

    def get_generic_item_by_id(self, generic_collection_name: str, id: int):
        return self.biocollections.get_generic_item(generic_collection_name, id)

    def create_generic_item(self, generic_collection_name: str, generic_item_data: dict):
        return self.biocollections.create_generic_item(generic_collection_name, generic_item_data)

    def update_generic_item(self, generic_collection_name: str, id: int, update_fields: dict):
        return self.biocollections.update_generic_item(generic_collection_name, id, update_fields)

    def delete_generic_item(self, generic_collection_name: str, id: int):
        return self.biocollections.delete_generic_item(generic_collection_name, id)

    def collection_to_df(self, generic_collection_name: str, fill_missing_with_none: bool = True):
        return self.biocollections.collection_to_df(generic_collection_name, fill_missing_with_none)

    # -- Plasmid methods --
    def get_plasmids_all(self):
        return self._get_list_all_pages(self.plasmids.get_all)

    def get_plasmid_by_id(self, id: int):
        return self.plasmids.get(id)

    def update_plasmid(self, id: int, update_fields: dict):
        return self.plasmids.update(id, update_fields)

    def create_plasmid(self, plasmid_data: dict):
        return self.plasmids.create(plasmid_data)

    def delete_plasmid(self, id: int):
        return self.plasmids.delete(id)

    # -- Protocol methods --
    def get_protocols_all(self):
        return self._get_list_all_pages(self.protocols.get_all)

    def get_protocol_by_id(self, id: int):
        return self.protocols.get(id)

    def update_protocol(self, id: int, update_fields: dict):
        return self.protocols.update(id, update_fields)

    def create_protocol(self, protocol_data: dict):
        return self.protocols.create(protocol_data)

    def delete_protocol(self, id: int):
        return self.protocols.delete(id)

    # -- SOP methods --
    def get_sops_all(self):
        return self._get_list_all_pages(self.sops.get_all)

    def get_sop_by_id(self, id: int):
        return self.sops.get(id)

    def update_sop(self, id: int, update_fields: dict):
        return self.sops.update(id, update_fields)

    def create_sop(self, sop_data: dict):
        return self.sops.create(sop_data)

    def delete_sop(self, id: int):
        return self.sops.delete(id)

    # -- Antibody methods --
    def get_antibodies_all(self):
        return self._get_list_all_pages(self.antibodies.get_all)

    def get_antibody_by_id(self, id: int):
        return self.antibodies.get(id)

    def update_antibody(self, id: int, update_fields: dict):
        return self.antibodies.update(id, update_fields)

    def create_antibody(self, antibody_data: dict):
        return self.antibodies.create(antibody_data)

    def delete_antibody(self, id: int):
        return self.antibodies.delete(id)

    # -- Cell line methods --
    def get_cell_lines_all(self):
        return self._get_list_all_pages(self.cell_lines.get_all)

    def get_cell_line_by_id(self, id: int):
        return self.cell_lines.get(id)

    def update_cell_line(self, id: int, update_fields: dict):
        return self.cell_lines.update(id, update_fields)

    def create_cell_line(self, cell_line_data: dict):
        return self.cell_lines.create(cell_line_data)

    def delete_cell_line(self, id: int):
        return self.cell_lines.delete(id)

    # -- Consumables methods --
    def get_consumables_all(self):
        return self._get_list_all_pages(self.consumables.get_all)

    def get_consumable_by_id(self, id: int):
        return self.consumables.get(id)

    def update_consumable(self, id: int, update_fields: dict):
        return self.consumables.update(id, update_fields)

    def create_consumable(self, consumable_data: dict):
        return self.consumables.create(consumable_data)

    def delete_consumable(self, id: int):
        return self.consumables.delete(id)

    # -- Primers methods --
    def get_primers_all(self):
        return self._get_list_all_pages(self.primers.get_all)

    def get_primer_by_id(self, id: int):
        return self.primers.get(id)

    def update_primer(self, id: int, update_fields: dict):
        return self.primers.update(id, update_fields)

    def create_primer(self, primer_data: dict):
        return self.primers.create(primer_data)

    def delete_primer(self, id: int):
        return self.primers.delete(id)

    # -- Plates methods --
    def get_plates_all(self):
        return self._get_list_all_pages(self.plates.get_all)

    def get_plate_by_id(self, id: int):
        return self.plates.get(id)

    def update_plate(self, id: int, update_fields: dict):
        return self.plates.update(id, update_fields)

    def create_plate(self, plate_data: dict):
        return self.plates.create(plate_data)

    def delete_plate(self, id: int):
        return self.plates.delete(id)


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

    def __init__(self, client: AuthenticatedClient, token: str, base_url: str):
        self.client = client
        self.token = token
        self.base_url = base_url

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
        response = requests.delete(f"{self.base_url}/api/v1/experiments/{experiment_id}?token={self.token}")
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

    def __init__(self, client: AuthenticatedClient, token: str, base_url: str):
        self.client = client
        self.token = token
        self.base_url = base_url

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
        response = requests.delete(f"{self.base_url}/api/v1/milestones/{folder_id}?token={self.token}")
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

    def __init__(self, client: AuthenticatedClient, token: str, base_url: str):
        self.client = client
        self.token = token
        self.base_url = base_url

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
        response = requests.delete(f"{self.base_url}/api/v1/projects/{project_id}?token={self.token}")
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

    def __init__(self, client: AuthenticatedClient, token: str, base_url: str):
        self.client = client
        self.token = token
        self.base_url = base_url

    def upload(self, file_path: Path | str, attach_to_uuid: str | Unset = UNSET, description: str | Unset = UNSET):
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

    def get_all(self, page: int = 1, meta: str = "false"):
        response = requests.get(f"{self.base_url}/api/v1/attachments?token={self.token}&page={page}&meta={meta}")
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving attachments: {response.status_code} - {json.loads(response.content)}")

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
        response = requests.delete(f"{self.base_url}/api/v1/attachments/{attachment_id}?token={self.token}")
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Error deleting attachment {attachment_id}: {response.status_code} - {response.content}")


class BiocollectionsAPI:
    """
    A dedicated class for biocollections-related endpoints.

    Provides methods for:
      - Filtering custom collection items
      - Listing generic items in a collection
      - Creating a new generic item
      - Updating a generic item
      - Retrieving a generic item by ID
      - Retrieving derived collections
    """

    def __init__(self, client: AuthenticatedClient, token: str, base_url: str):
        self.client = client
        self.token = token
        self.base_url = base_url

    def filter_items(
        self,
        collection_name: str,
        filter_field: str,
        filter_operator: str,
        filter_value: str,
        page: int = 1,
        meta: str = "true",
        kendo: str = "true",
        filter_logic: str = "and",
    ):
        """
        Filter custom collection items by applying a filter.

        :param collection_name: The collection name to filter (e.g. 'myCollection').
        :param filter_field: Field to filter on. Valid fields are: title, auto_name(SySID), alternative_name, description, owner_id
        :param filter_operator: Filter operator (e.g. 'contains').
        :param filter_value: Value to filter by.
        :param page: Page number (default 1).
        :param meta: 'true' or 'false' to include summarized metadata.
        :param kendo: 'true' (required).
        :param filter_logic: Logic operator between filters (default 'and').
        """
        response = get_api_v1_biocollections_collection_name.sync_detailed(
            client=self.client,
            token=self.token,
            page=page,
            meta=meta,
            kendo=kendo,
            collection_name=collection_name,
            filterlogic=filter_logic,
            filterfilters0field=filter_field,
            filterfilters0operator=filter_operator,
            filterfilters0value=filter_value,
        )
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error filtering collection '{collection_name}': {response.status_code} - {json.loads(response.content)}")

    def get_generic_items(self, generic_collection_name: str, page: int = 1, meta: str = "true"):
        """
        List all generic items in the specified collection.

        :param generic_collection_name: The generic collection name.
        :param page: Page number (default 1).
        :param meta: 'true' or 'false' to include summarized metadata.
        """
        response = get_api_v1_biocollections_generic_collection_name.sync_detailed(
            client=self.client,
            token=self.token,
            generic_collection_name=generic_collection_name,
            page=page,
            meta=meta,
        )
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error retrieving generic items for collection '{generic_collection_name}': {response.status_code} - {json.loads(response.content)}"
            )

    def create_generic_item(self, generic_collection_name: str, generic_item_data: dict):
        """
        Create a new generic item in the specified collection.

        :param generic_collection_name: The generic collection name.
        :param generic_item_data: Dictionary with the item data.
        """
        item = CreateGenericItemItem.from_dict(generic_item_data)
        payload = CreateGenericItem(token=self.token, item=item)  # type: ignore
        response = post_api_v1_biocollections_generic_collection_name.sync_detailed(
            client=self.client, generic_collection_name=generic_collection_name, body=payload
        )
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error creating generic item in collection '{generic_collection_name}': {response.status_code} - {json.loads(response.content)}"
            )

    def update_generic_item(self, generic_collection_name: str, id: int, update_fields: dict):
        """
        Update a generic item in the specified collection.

        :param generic_collection_name: The generic collection name.
        :param id: The ID of the generic item.
        :param update_fields: Dictionary with the fields to update.
        """
        update_item = UpdateGenericItemItem.from_dict(update_fields)
        payload = UpdateGenericItem(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_biocollections_generic_collection_name_id.sync_detailed(
            client=self.client, generic_collection_name=generic_collection_name, id=id, body=payload
        )
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error updating generic item {id} in collection '{generic_collection_name}': {response.status_code} - {json.loads(response.content)}"
            )

    def get_generic_item(self, generic_collection_name: str, id: int):
        """
        Retrieve a generic item by ID from the specified collection.

        :param generic_collection_name: The generic collection name.
        :param id: The ID of the generic item.
        """
        response = get_api_v1_biocollections_generic_collection_name_id.sync_detailed(
            client=self.client, token=self.token, generic_collection_name=generic_collection_name, id=id
        )
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(
                f"Error retrieving generic item {id} in collection '{generic_collection_name}': {response.status_code} - {json.loads(response.content)}"
            )

    def delete_generic_item(self, generic_collection_name: str, id: int):
        """
        Delete a generic item by ID from the specified collection.

        :param generic_collection_name: The generic collection name.
        :param id: The ID of the generic item.
        """
        response = requests.delete(f"{self.base_url}/api/v1/biocollections/{generic_collection_name}/{id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(
                f"Error deleting generic item {id} in collection '{generic_collection_name}': {response.status_code} - {response.content}"
            )

    def collection_to_df(self, collection_name: str, fill_missing_with_none: bool = True):
        """
        Get a pandas dataframe out of a labguru collection.

        :param collection_name: The name of the collection in labguru
        :param fill_missing_with_none: If True, fill missing strings with None
        :return: pandas DataFrame representing the collection
        """
        # returns list of dict
        labguru_api = LabguruAPI()
        collection_items = labguru_api.get_generic_items_all(collection_name)

        fixed_columns = ["id", "name", "auto_name", "created_at", "updated_at", "updated_by"]

        # table-specific columns
        all_keys = list(collection_items[0].keys())
        key_index_0 = [i for i, key in enumerate(all_keys) if key == "tags"][0]
        key_index_1 = [i for i, key in enumerate(all_keys) if key == "sys_id"][0]
        specific_columns = all_keys[key_index_0 + 1 : key_index_1]

        extract_columns = fixed_columns + specific_columns
        sub_dict = [{k: v for k, v in item.items() if k in extract_columns} for item in collection_items]
        collection_df = pd.DataFrame.from_dict(sub_dict)

        # nested columns
        collection_df["owner"] = [item["owner"]["name"] for item in collection_items]

        # parent information
        if collection_items[0]["parents"] is not None:
            for parent_name, parent_dict in collection_items[0]["parents"].items():
                # not sure why this is a list of dict, it should just be one column
                parent_dict = parent_dict[0]
                column_name = parent_dict["parent_collection"]
                assert column_name not in collection_df.columns
                collection_df[column_name] = [item["parents"][parent_name][0]["parent_title"] for item in collection_items]

        # remove unnecessary column starting with Biocollections::GenericCollection
        collection_df = collection_df.loc[:, ~collection_df.columns.str.startswith("Biocollections::GenericCollection")]

        # fill missing strings with None
        if fill_missing_with_none:
            collection_df = collection_df.map(lambda x: None if x == "" else x)

        # re-order columns to have the system columns at the back
        system_columns = ["auto_name", "created_at", "owner", "updated_at", "updated_by"]
        collection_df = collection_df[[col for col in collection_df.columns if col not in system_columns] + system_columns]

        collection_df.set_index("id", inplace=True)

        return collection_df


class PlasmidsAPI:
    """
    A dedicated class for plasmid-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(plasmid_id)
        - update(plasmid_id, update_fields)
        - create(plasmid_data)
    """

    def __init__(self, client: AuthenticatedClient, token: str, base_url: str):
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        response = get_api_v1_plasmids.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving plasmids: {response.status_code} - {json.loads(response.content)}")

    def get(self, plasmid_id: int):
        response = get_api_v1_plasmids_id.sync_detailed(client=self.client, token=self.token, id=plasmid_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving plasmid {plasmid_id}: {response.status_code} - {json.loads(response.content)}")

    def update(self, plasmid_id: int, update_fields: dict):
        """
        Update a plasmid.

        :param plasmid_id: The ID of the plasmid to update.
        :param update_fields: Dictionary with the fields to update.
        :return: The updated plasmid data.
        """
        updated_plasmid_item = UpdatePlasmidItem.from_dict(update_fields)
        updated_plasmid_payload = UpdatePlasmid(token=self.token, item=updated_plasmid_item)  # type: ignore
        response = put_api_v1_plasmids_id.sync_detailed(client=self.client, id=plasmid_id, body=updated_plasmid_payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating plasmid {plasmid_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, plasmid_data: dict):
        """
        Create a new plasmid.

        :param plasmid_data: Dictionary with plasmid fields.
        :return: The created plasmid data.
        """
        create_plasmid_item = CreatePlasmidItem.from_dict(plasmid_data)
        create_plasmid_payload = CreatePlasmid(token=self.token, item=create_plasmid_item)  # type: ignore
        response = post_api_v1_plasmids.sync_detailed(client=self.client, body=create_plasmid_payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating plasmid: {response.status_code} - {json.loads(response.content)}")

    def delete(self, plasmid_id: int):
        """
        Delete a plasmid.

        :param plasmid_id: The ID of the plasmid to delete.
        :return: True if successful, otherwise an exception is raised.
        """
        response = requests.delete(f"{self.base_url}/api/v1/plasmids/{plasmid_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting plasmid {plasmid_id}: {response.status_code} - {response.content}")


class ProtocolsAPI:
    """
    A dedicated class for protocol-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(protocol_id)
        - create(protocol_data)
        - update(protocol_id, update_fields)
        - delete(protocol_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the ProtocolsAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all protocols.

        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing protocols data.
        """
        response = get_api_v1_protocols.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving protocols: {response.status_code} - {json.loads(response.content)}")

    def get(self, protocol_id: int):
        """
        Retrieve a protocol by its ID.

        :param protocol_id: The ID of the protocol to retrieve.
        :return: A JSON object containing the protocol data.
        """
        response = get_api_v1_protocols_id.sync_detailed(client=self.client, token=self.token, id=protocol_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving protocol {protocol_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, protocol_data: dict):
        """
        Create a new protocol.

        :param protocol_data: Dictionary with protocol fields.
        :return: A JSON object containing the created protocol data.
        """
        raise NotImplementedError("Create protocol not implemented yet.")
        # protocol_item = CreateProtocolItem.from_dict(protocol_data)
        # payload = CreateProtocol(token=self.token, item=protocol_item)  # type: ignore
        # response = post_api_v1_protocols.sync_detailed(client=self.client, body=payload)
        # if response.status_code in (200, 201):
        #     return json.loads(response.content)
        # else:
        #     raise Exception(f"Error creating protocol: {response.status_code} - {json.loads(response.content)}")

    def update(self, protocol_id: int, update_fields: dict):
        """
        Update an existing protocol.

        :param protocol_id: The ID of the protocol to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated protocol data.
        """
        update_item = UpdateProtocolItem.from_dict(update_fields)
        payload = UpdateProtocol(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_protocols_id.sync_detailed(client=self.client, id=protocol_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating protocol {protocol_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, protocol_id: int):
        """
        Delete a protocol.

        :param protocol_id: The ID of the protocol to delete.
        :return: True if the protocol was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/protocols/{protocol_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting protocol {protocol_id}: {response.status_code} - {json.loads(response.content)}")


class SopsAPI:
    """
    A dedicated class for SOPs-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(sop_id)
        - create(sop_data)
        - update(sop_id, update_fields)
        - delete(sop_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the SopsAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all SOPs.

        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing SOPs data.
        """
        response = get_api_v1_sops.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving SOPs: {response.status_code} - {json.loads(response.content)}")

    def get(self, sop_id: int):
        """
        Retrieve a SOP by its ID.

        :param sop_id: The ID of the SOP to retrieve.
        :return: A JSON object containing the SOP data.
        """
        response = get_api_v1_sops_id.sync_detailed(client=self.client, token=self.token, id=sop_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving SOP {sop_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, sop_data: dict):
        """
        Create a new SOP.

        :param sop_data: Dictionary with SOP fields.
        :return: A JSON object containing the created SOP data.
        """

        sop_item = CreateSOPItem.from_dict(sop_data)
        payload = CreateSOP(token=self.token, item=sop_item)  # type: ignore
        response = post_api_v1_sops.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating SOP: {response.status_code} - {json.loads(response.content)}")

    def update(self, sop_id: int, update_fields: dict):
        """
        Update an existing SOP.

        :param sop_id: The ID of the SOP to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated SOP data.
        """

        update_item = UpdateSOPItem.from_dict(update_fields)
        payload = UpdateSOP(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_sops_id.sync_detailed(client=self.client, id=sop_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating SOP {sop_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, sop_id: int):
        """
        Delete a SOP.

        :param sop_id: The ID of the SOP to delete.
        :return: True if the SOP was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/sops/{sop_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting SOP {sop_id}: {response.status_code} - {response.content}")


class AntibodiesAPI:
    """
    A dedicated class for antibodies-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(antibody_id)
        - create(antibody_data)
        - update(antibody_id, update_fields)
        - delete(antibody_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the AntibodiesAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all antibodies.

        :param page: Page number (default is 1).
        :param
        meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing antibodies data.
        """
        response = get_api_v1_antibodies.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving antibodies: {response.status_code} - {json.loads(response.content)}")

    def get(self, antibody_id: int):
        """
        Retrieve a antibody by its ID.

        :param antibody_id: The ID of the antibody to retrieve.
        :return: A JSON object containing the antibody data.
        """
        response = get_api_v1_antibodies_id.sync_detailed(client=self.client, token=self.token, id=antibody_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving antibody {antibody_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, antibody_data: dict):
        """
        Create a new antibody.

        :param antibody_data: Dictionary with antibody fields.
        :return: A JSON object containing the created antibody data.
        """
        antibody_item = CreateAntibodyItem.from_dict(antibody_data)
        payload = CreateAntibody(token=self.token, item=antibody_item)  # type: ignore
        response = post_api_v1_antibodies.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating antibody: {response.status_code} - {json.loads(response.content)}")

    def update(self, antibody_id: int, update_fields: dict):
        """
        Update an existing antibody.

        :param antibody_id: The ID of the antibody to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated antibody data.
        """
        update_item = UpdateAntibodyItem.from_dict(update_fields)
        payload = UpdateAntibody(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_antibodies_id.sync_detailed(client=self.client, id=antibody_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating antibody {antibody_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, antibody_id: int):
        """
        Delete a antibody.

        :param antibody_id: The ID of the antibody to delete.
        :return: True if the antibody was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/antibodies/{antibody_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting antibody {antibody_id}: {response.status_code} - {response.content}")


class CellLinesAPI:
    """
    A dedicated class for cell lines-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(cell_line_id)
        - create(cell_line_data)
        - update(cell_line_id, update_fields)
        - delete(cell_line_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the CellLinesAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all cell lines.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing cell lines data.
        """
        response = get_api_v1_cell_lines.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving cell lines: {response.status_code} - {json.loads(response.content)}")

    def get(self, cell_line_id: int):
        """
        Retrieve a cell line by its ID.

        :param cell_line_id: The ID of the cell line to retrieve.
        :return: A JSON object containing the cell line data.
        """
        response = get_api_v1_cell_lines_id.sync_detailed(client=self.client, token=self.token, id=cell_line_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving cell line {cell_line_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, cell_line_data: dict):
        """
        Create a new cell line.

        :param cell_line_data: Dictionary with cell line fields.
        :return: A JSON object containing the created cell line data.
        """
        cell_line_item = CreateCellLineItem.from_dict(cell_line_data)
        payload = CreateCellLine(token=self.token, item=cell_line_item)  # type: ignore
        response = post_api_v1_cell_lines.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating cell line: {response.status_code} - {json.loads(response.content)}")

    def update(self, cell_line_id: int, update_fields: dict):
        """
        Update an existing cell line.

        :param cell_line_id: The ID of the cell line to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated cell line data.
        """
        update_item = UpdateCellLineItem.from_dict(update_fields)
        payload = UpdateCellLine(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_cell_lines_id.sync_detailed(client=self.client, id=cell_line_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating cell line {cell_line_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, cell_line_id: int):
        """
        Delete a cell line.

        :param cell_line_id: The ID of the cell line to delete.
        :return: True if the cell line was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/cell_lines/{cell_line_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting cell line {cell_line_id}: {response.status_code} - {response.content}")


class ConsumablesAPI:
    """
    A dedicated class for consumables-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(consumable_id)
        - create(consumable_data)
        - update(consumable_id, update_fields)
        - delete(consumable_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the ConsumablesAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all consumables.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing consumables data.
        """
        response = get_api_v1_materials.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving consumables: {response.status_code} - {json.loads(response.content)}")

    def get(self, consumable_id: int):
        """
        Retrieve a consumable by its ID.

        :param consumable_id: The ID of the consumable to retrieve.
        :return: A JSON object containing the consumable data.
        """
        response = get_api_v1_materials_id.sync_detailed(client=self.client, token=self.token, id=consumable_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving consumable {consumable_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, consumable_data: dict):
        """
        Create a new consumable.

        :param consumable_data: Dictionary with consumable fields.
        :return: A JSON object containing the created consumable data.
        """
        consumable_item = CreateMaterialItem.from_dict(consumable_data)
        payload = CreateMaterial(token=self.token, item=consumable_item)  # type: ignore
        response = post_api_v1_materials.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating consumable: {response.status_code} - {json.loads(response.content)}")

    def update(self, consumable_id: int, update_fields: dict):
        """
        Update an existing consumable.

        :param consumable_id: The ID of the consumable to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated consumable data.
        """
        update_item = UpdateMaterialItem.from_dict(update_fields)
        payload = UpdateMaterial(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_materials_id.sync_detailed(client=self.client, id=consumable_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating consumable {consumable_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, consumable_id: int):
        """
        Delete a consumable.

        :param consumable_id: The ID of the consumable to delete.
        :return: True if the consumable was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/materials/{consumable_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting consumable {consumable_id}: {response.status_code} - {response.content}")


class PrimersAPI:
    """
    A dedicated class for primers
    Provides methods:
        - get_all(page, meta)
        - get(primer_id)
        - create(primer_data)
        - update(primer_id, update_fields)
        - delete(primer_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the PrimersAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all primers.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing primers data.
        """
        response = get_api_v1_primers.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving primers: {response.status_code} - {json.loads(response.content)}")

    def get(self, primer_id: int):
        """
        Retrieve a primer by its ID.

        :param primer_id: The ID of the primer to retrieve.
        :return: A JSON object containing the primer data.
        """
        response = get_api_v1_primers_id.sync_detailed(client=self.client, token=self.token, id=primer_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving primer {primer_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, primer_data: dict):
        """
        Create a new primer.

        :param primer_data: Dictionary with primer fields.
        :return: A JSON object containing the created primer data.
        """
        primer_item = CreatePrimerItem.from_dict(primer_data)
        payload = CreatePrimer(token=self.token, item=primer_item)  # type: ignore
        response = post_api_v1_primers.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating primer: {response.status_code} - {json.loads(response.content)}")

    def update(self, primer_id: int, update_fields: dict):
        """
        Update an existing primer.

        :param primer_id: The ID of the primer to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated primer data.
        """
        update_item = UpdatePrimerItem.from_dict(update_fields)
        payload = UpdatePrimer(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_primers_id.sync_detailed(client=self.client, id=primer_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating primer {primer_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, primer_id: int):
        """
        Delete a primer.

        :param primer_id: The ID of the primer to delete.
        :return: True if the primer was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/primers/{primer_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting primer {primer_id}: {response.status_code} - {response.content}")


class PlatesAPI:
    """
    A dedicated class for plates-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(plate_id)
        - create(plate_data)
        - update(plate_id, update_fields)
        - delete(plate_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the PlatesAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all plates.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing plates data.
        """
        response = get_api_v1_plates.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving plates: {response.status_code} - {json.loads(response.content)}")

    def get(self, plate_id: int):
        """
        Retrieve a plate by its ID.

        :param plate_id: The ID of the plate to retrieve.
        :return: A JSON object containing the plate data.
        """
        response = get_api_v1_plates_id.sync_detailed(client=self.client, token=self.token, id=plate_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving plate {plate_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, plate_data: dict):
        """
        Create a new plate.

        :param plate_data: Dictionary with plate fields.
        :return: A JSON object containing the created plate data.
        """
        raise NotImplementedError("Create plate not implemented yet.")
        plate_item = CreatePlateItem.from_dict(plate_data)  # type: ignore
        payload = CreatePlate(token=self.token, item=plate_item)  # type: ignore
        response = post_api_v1_plates.sync_detailed(client=self.client, body=payload)  # type: ignore
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating plate: {response.status_code} - {json.loads(response.content)}")

    def update(self, plate_id: int, update_fields: dict):
        """
        Update an existing plate.

        :param plate_id: The ID of the plate to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated plate data.
        """
        raise NotImplementedError("Update plate not implemented yet.")
        update_item = UpdatePlateItem.from_dict(update_fields)  # type: ignore
        payload = UpdatePlate(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_plates_id.sync_detailed(client=self.client, id=plate_id, body=payload)  # type: ignore
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating plate {plate_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, plate_id: int):
        """
        Delete a plate.

        :param plate_id: The ID of the plate to delete.
        :return: True if the plate was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/plates/{plate_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting plate {plate_id}: {response.status_code} - {response.content}")


class StocksAPI:
    """
    A dedicated class for stocks-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(stock_id)
        - create(stock_data)
        - update(stock_id, update_fields)
        - delete(stock_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the StocksAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all stocks.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing stocks data.
        """
        response = get_api_v1_stocks.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving stocks: {response.status_code} - {json.loads(response.content)}")

    def get(self, stock_id: int):
        """
        Retrieve a stock by its ID.

        :param stock_id: The ID of the stock to retrieve.
        :return: A JSON object containing the stock data.
        """
        response = get_api_v1_stocks_id.sync_detailed(client=self.client, token=self.token, id=stock_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving stock {stock_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, stock_data: dict):
        """
        Create a new stock.

        :param stock_data: Dictionary with stock fields.
        :return: A JSON object containing the created stock data.
        """
        stock_item = CreateStockItem.from_dict(stock_data)
        payload = CreateStock(token=self.token, item=stock_item)  # type: ignore
        response = post_api_v1_stocks.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating stock: {response.status_code} - {json.loads(response.content)}")

    def update(self, stock_id: int, update_fields: dict):
        """
        Update an existing stock.

        :param stock_id: The ID of the stock to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated stock data.
        """
        update_item = UpdateStockItem.from_dict(update_fields)
        payload = UpdateStock(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_stocks_id.sync_detailed(client=self.client, id=stock_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating stock {stock_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, stock_id: int):
        """
        Delete a stock.

        :param stock_id: The ID of the stock to delete.
        :return: True if the stock was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/stocks/{stock_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting stock {stock_id}: {response.status_code} - {response.content}")


class StoragesAPI:
    """
    A dedicated class for storages-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(storage_id)
        - create(storage_data)
        - update(storage_id, update_fields)
        - delete(storage_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the StoragesAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all storages.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing storages data.
        """
        response = get_api_v1_storages.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving storages: {response.status_code} - {json.loads(response.content)}")

    def get(self, storage_id: int):
        """
        Retrieve a storage by its ID.

        :param storage_id: The ID of the storage to retrieve.
        :return: A JSON object containing the storage data.
        """
        response = get_api_v1_storages_id.sync_detailed(client=self.client, token=self.token, id=storage_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving storage {storage_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, storage_data: dict):
        """
        Create a new storage.

        :param storage_data: Dictionary with storage fields.
        :return: A JSON object containing the created storage data.
        """
        storage_item = CreateStorageItem.from_dict(storage_data)
        payload = CreateStorage(token=self.token, item=storage_item)
        response = post_api_v1_storages.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating storage: {response.status_code} - {json.loads(response.content)}")

    def update(self, storage_id: int, update_fields: dict):
        """
        Update an existing storage.

        :param storage_id: The ID of the storage to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated storage data.
        """
        update_item = UpdateStorageItem.from_dict(update_fields)
        payload = UpdateStorage(token=self.token, item=update_item)
        response = put_api_v1_storages_id.sync_detailed(client=self.client, id=storage_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating storage {storage_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, storage_id: int):
        """
        Delete a storage.

        :param storage_id: The ID of the storage to delete.
        :return: True if the storage was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/storages/{storage_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting storage {storage_id}: {response.status_code} - {response.content}")


class SequencesAPI:
    """
    A dedicated class for sequences-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(sequence_id)
        - create(sequence_data)
        - update(sequence_id, update_fields)
        - delete(sequence_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the SequencesAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all sequences.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing sequences data.
        """
        response = get_api_v1_sequences.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving sequences: {response.status_code} - {json.loads(response.content)}")

    def get(self, sequence_id: int):
        """
        Retrieve a sequence by its ID.

        :param sequence_id: The ID of the sequence to retrieve.
        :return: A JSON object containing the sequence data.
        """
        response = get_api_v1_sequences_id.sync_detailed(client=self.client, token=self.token, id=sequence_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving sequence {sequence_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, sequence_data: dict):
        """
        Create a new sequence.

        :param sequence_data: Dictionary with sequence fields.
        :return: A JSON object containing the created sequence data.
        """
        sequence_item = CreateSequenceItem.from_dict(sequence_data)
        payload = CreateSequence(token=self.token, item=sequence_item)  # type: ignore
        response = post_api_v1_sequences.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating sequence: {response.status_code} - {json.loads(response.content)}")

    def update(self, sequence_id: int, update_fields: dict):
        """
        Update an existing sequence.

        :param sequence_id: The ID of the sequence to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated sequence data.
        """
        update_item = UpdateSequenceItem.from_dict(update_fields)
        payload = UpdateSequence(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_sequences_id.sync_detailed(client=self.client, id=sequence_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating sequence {sequence_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, sequence_id: int):
        """
        Delete a sequence.

        :param sequence_id: The ID of the sequence to delete.
        :return: True if the sequence was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/sequences/{sequence_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting sequence {sequence_id}: {response.status_code} - {response.content}")


class ProteinsAPI:
    """
    A dedicated class for proteins-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(protein_id)
        - create(protein_data)
        - update(protein_id, update_fields)
        - delete(protein_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the ProteinsAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all proteins.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing proteins data.
        """
        response = get_api_v1_proteins.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving proteins: {response.status_code} - {json.loads(response.content)}")

    def get(self, protein_id: int):
        """
        Retrieve a protein by its ID.

        :param protein_id: The ID of the protein to retrieve.
        :return: A JSON object containing the protein data.
        """
        response = get_api_v1_proteins_id.sync_detailed(client=self.client, token=self.token, id=protein_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving protein {protein_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, protein_data: dict):
        """
        Create a new protein.

        :param protein_data: Dictionary with protein fields.
        :return: A JSON object containing the created protein data.
        """
        protein_item = CreateProteinItem.from_dict(protein_data)
        payload = CreateProtein(token=self.token, item=protein_item)  # type: ignore
        response = post_api_v1_proteins.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating protein: {response.status_code} - {json.loads(response.content)}")

    def update(self, protein_id: int, update_fields: dict):
        """
        Update an existing protein.

        :param protein_id: The ID of the protein to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated protein data.
        """
        update_item = UpdateProteinItem.from_dict(update_fields)
        payload = UpdateProtein(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_proteins_id.sync_detailed(client=self.client, id=protein_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating protein {protein_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, protein_id: int):
        """
        Delete a protein.

        :param protein_id: The ID of the protein to delete.
        :return: True if the protein was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/proteins/{protein_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting protein {protein_id}: {response.status_code} - {response.content}")


class EquipmentAPI:
    """
    A dedicated class for equipment-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(equipment_id)
        - create(equipment_data)
        - update(equipment_id, update_fields)
        - delete(equipment_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the EquipmentAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all equipment.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing equipment data.
        """
        response = get_api_v1_instruments.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving equipment: {response.status_code} - {json.loads(response.content)}")

    def get(self, equipment_id: int):
        """
        Retrieve a equipment by its ID.

        :param equipment_id: The ID of the equipment to retrieve.
        :return: A JSON object containing the equipment data.
        """
        response = get_api_v1_instruments_id.sync_detailed(client=self.client, token=self.token, id=equipment_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving equipment {equipment_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, equipment_data: dict):
        """
        Create a new equipment.

        :param equipment_data: Dictionary with equipment fields.
        :return: A JSON object containing the created equipment data.
        """
        raise NotImplementedError("Create equipment not implemented yet.")
        equipment_item = CreateInstrumentItem.from_dict(equipment_data)  # type: ignore
        payload = CreateInstrument(token=self.token, item=equipment_item)  # type: ignore
        response = post_api_v1_instruments.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating equipment: {response.status_code} - {json.loads(response.content)}")

    def update(self, equipment_id: int, update_fields: dict):
        """
        Update an existing equipment.

        :param equipment_id: The ID of the equipment to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated equipment data.
        """
        raise NotImplementedError("Update equipment not implemented yet.")
        update_item = UpdateInstrumentItem.from_dict(update_fields)  # type: ignore
        payload = UpdateInstrument(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_instruments_id.sync_detailed(client=self.client, id=equipment_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating equipment {equipment_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, equipment_id: int):
        """
        Delete a equipment.

        :param equipment_id: The ID of the equipment to delete.
        :return: True if the equipment was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/instruments/{equipment_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting equipment {equipment_id}: {response.status_code} - {response.content}")


class DatasetsAPI:
    """
    A dedicated class for datasets-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(dataset_id)
        - create(dataset_data)
        - update(dataset_id, update_fields)
        - delete(dataset_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the DatasetsAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all datasets.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing datasets data.
        """
        response = get_api_v1_datasets.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving datasets: {response.status_code} - {json.loads(response.content)}")

    def get(self, dataset_id: int):
        """
        Retrieve a dataset by its ID.

        :param dataset_id: The ID of the dataset to retrieve.
        :return: A JSON object containing the dataset data.
        """
        response = get_api_v1_datasets_id.sync_detailed(client=self.client, token=self.token, id=dataset_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving dataset {dataset_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, dataset_data: dict):
        """
        Create a new dataset.

        :param dataset_data: Dictionary with dataset fields.
        :return: A JSON object containing the created dataset data.
        """
        dataset_item = CreateDatasetItem.from_dict(dataset_data)
        payload = CreateDataset(token=self.token, item=dataset_item)
        response = post_api_v1_datasets.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating dataset: {response.status_code} - {json.loads(response.content)}")

    def update(self, dataset_id: int, update_fields: dict):
        """
        Update an existing dataset.

        :param dataset_id: The ID of the dataset to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated dataset data.
        """
        raise NotImplementedError("Update dataset not implemented yet.")
        update_item = UpdateDatasetItem.from_dict(update_fields)  # type: ignore
        payload = UpdateDataset(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_datasets_id.sync_detailed(client=self.client, id=dataset_id, body=payload)  # type: ignore
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating dataset {dataset_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, dataset_id: int):
        """
        Delete a dataset.

        :param dataset_id: The ID of the dataset to delete.
        :return: True if the dataset was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/datasets/{dataset_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting dataset {dataset_id}: {response.status_code} - {response.content}")


class BoxesAPI:
    """
    A dedicated class for boxes-related endpoints.

    Provides methods:
        - get_all(page, meta)
        - get(box_id)
        - create(box_data)
        - update(box_id, update_fields)
        - delete(box_id)
    """

    def __init__(self, client, token: str, base_url: str):
        """
        Initialize the BoxesAPI.

        :param client: An instance of AuthenticatedClient.
        :param token: API authentication token.
        """
        self.client = client
        self.token = token
        self.base_url = base_url

    def get_all(self, page: int = 1, meta: str = "false"):
        """
        Retrieve all boxes.
        :param page: Page number (default is 1).
        :param meta: Include metadata flag ('true' or 'false').
        :return: A JSON object containing boxes data.
        """
        response = get_api_v1_boxes.sync_detailed(client=self.client, token=self.token, page=page, meta=meta)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving boxes: {response.status_code} - {json.loads(response.content)}")

    def get(self, box_id: int):
        """
        Retrieve a box by its ID.

        :param box_id: The ID of the box to retrieve.
        :return: A JSON object containing the box data.
        """
        response = get_api_v1_boxes_id.sync_detailed(client=self.client, token=self.token, id=box_id)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error retrieving box {box_id}: {response.status_code} - {json.loads(response.content)}")

    def create(self, box_data: dict):
        """
        Create a new box.

        :param box_data: Dictionary with box fields.
        :return: A JSON object containing the created box data.
        """
        box_item = CreateBoxItem.from_dict(box_data)
        payload = CreateBox(token=self.token, item=box_item)  # type: ignore
        response = post_api_v1_boxes.sync_detailed(client=self.client, body=payload)
        if response.status_code in (200, 201):
            return json.loads(response.content)
        else:
            raise Exception(f"Error creating box: {response.status_code} - {json.loads(response.content)}")

    def update(self, box_id: int, update_fields: dict):
        """
        Update an existing box.

        :param box_id: The ID of the box to update.
        :param update_fields: Dictionary with the fields to update.
        :return: A JSON object containing the updated box data.
        """
        update_item = UpdateBoxItem.from_dict(update_fields)
        payload = UpdateBox(token=self.token, item=update_item)  # type: ignore
        response = put_api_v1_boxes_id.sync_detailed(client=self.client, id=box_id, body=payload)
        if response.status_code in (200, 204):
            return json.loads(response.content)
        else:
            raise Exception(f"Error updating box {box_id}: {response.status_code} - {json.loads(response.content)}")

    def delete(self, box_id: int):
        """
        Delete a box.

        :param box_id: The ID of the box to delete.
        :return: True if the box was successfully deleted.
        """
        response = requests.delete(f"{self.base_url}/api/v1/boxes/{box_id}?token={self.token}")
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Error deleting box {box_id}: {response.status_code} - {response.content}")
