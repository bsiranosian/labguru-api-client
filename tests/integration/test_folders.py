import os
import pytest
from pathlib import Path
from labguru_wrapper.labguru_api import LabguruAPI
from tests import test_settings


@pytest.fixture(scope="module")
def labguru_api():
    env_file = os.getenv("LABGURU_TEST_ENV", Path.home() / ".labguru.test.env")
    return LabguruAPI(env_file=env_file)


@pytest.mark.integration
def test_get_all_folders(labguru_api):
    folders = labguru_api.get_all_folders(page=1, meta="false")
    assert isinstance(folders, (dict, list)), "Response should be a dict or list."


@pytest.mark.integration
def test_get_folder(labguru_api):
    folder_id = test_settings.FOLDER_TO_MODIFY
    folder = labguru_api.get_folder(folder_id)
    assert folder.get("id") == folder_id, f"Retrieved folder id {folder.get('id')} does not match expected {folder_id}."


@pytest.mark.integration
def test_update_folder(labguru_api):
    folder_id = test_settings.FOLDER_TO_MODIFY
    original_folder = labguru_api.get_folder(folder_id)
    original_title = original_folder.get("title")
    update_fields = {"title": "Updated Folder title by Integration Test"}
    labguru_api.update_folder(folder_id, update_fields)
    updated_folder = labguru_api.get_folder(folder_id)
    assert updated_folder.get("title") == update_fields["title"], "Folder title was not updated."

    # Revert to original
    revert_fields = {"title": original_title}
    labguru_api.update_folder(folder_id, revert_fields)
    reverted_folder = labguru_api.get_folder(folder_id)
    assert reverted_folder.get("title") == original_title, "Folder title was not reverted."


@pytest.mark.integration
def test_create_and_delete_folder(labguru_api):
    payload = test_settings.CREATE_FOLDER_PAYLOAD
    created_folder = labguru_api.create_folder(folder_data=payload)
    assert "id" in created_folder, "Created folder does not have an 'id'."
    folder_id = created_folder["id"]

    retrieved_folder = labguru_api.get_folder(folder_id)
    assert retrieved_folder.get("title") == payload["title"], "Folder title does not match."

    labguru_api.delete_folder(folder_id)
    with pytest.raises(Exception):
        labguru_api.get_folder(folder_id)
