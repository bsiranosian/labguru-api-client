import os
import pytest
from pathlib import Path
from labguru_wrapper.labguru_api import LabguruAPI
from tests import test_settings


@pytest.fixture(scope="module")
def labguru_api():
    """
    Instantiate LabguruAPI using a test-specific environment file.
    """
    env_file = os.getenv("LABGURU_TEST_ENV", Path.home() / ".labguru.test.env")
    return LabguruAPI(env_file=env_file)


@pytest.mark.integration
def test_get_all_plasmids(labguru_api):
    plasmids = labguru_api.get_all_plasmids(page=1, meta="false")
    assert isinstance(plasmids, (dict, list)), "Response should be a dict or list."


@pytest.mark.integration
def test_get_plasmid(labguru_api):
    plasmid_id = test_settings.ALLOWED_PLASMID_IDS[0]
    plasmid = labguru_api.get_plasmid(plasmid_id)
    assert plasmid.get("id") == plasmid_id, f"Retrieved plasmid id {plasmid.get('id')} does not match expected {plasmid_id}."


@pytest.mark.integration
def test_update_plasmid(labguru_api):
    plasmid_id = test_settings.PLASMID_TO_MODIFY
    original_plasmid = labguru_api.get_plasmid(plasmid_id)
    original_title = original_plasmid.get("title")
    update_fields = {"title": "Updated Title by Integration Test"}
    updated_plasmid = labguru_api.update_plasmid(plasmid_id, update_fields)
    assert updated_plasmid.get("title") == update_fields["title"], "Experiment title was not updated."

    # Revert to original
    revert_fields = {"title": original_title}
    reverted_plasmid = labguru_api.update_plasmid(plasmid_id, revert_fields)
    assert reverted_plasmid.get("title") == original_title, "Experiment title was not reverted."


@pytest.mark.integration
def test_create_and_delete_plasmid(labguru_api):
    payload = test_settings.CREATE_PLASMID_PAYLOAD
    created_plasmid = labguru_api.create_plasmid(plasmid_data=payload)
    assert "id" in created_plasmid, "Created plasmid does not have an 'id'."
    plasmid_id = created_plasmid["id"]

    retrieved_plasmid = labguru_api.get_plasmid(plasmid_id)
    assert retrieved_plasmid.get("title") == payload["title"], "Experiment title does not match."

    labguru_api.delete_plasmid(plasmid_id)
    with pytest.raises(Exception):
        labguru_api.get_plasmid(plasmid_id)
