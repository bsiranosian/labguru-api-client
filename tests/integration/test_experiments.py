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
def test_get_experiments_all(labguru_api):
    experiments = labguru_api.get_experiments_all()
    assert isinstance(experiments, (dict, list)), "Response should be a dict or list."


@pytest.mark.integration
def test_get_experiment_by_id(labguru_api):
    experiment_id = test_settings.ALLOWED_EXPERIMENT_IDS[0]
    experiment = labguru_api.get_experiment_by_id(experiment_id)
    assert experiment.get("id") == experiment_id, f"Retrieved experiment id {experiment.get('id')} does not match expected {experiment_id}."


@pytest.mark.integration
def test_update_experiment(labguru_api):
    experiment_id = test_settings.EXPERIMENT_TO_MODIFY
    original_experiment = labguru_api.get_experiment_by_id(experiment_id)
    original_title = original_experiment.get("title")
    update_fields = {"title": "Updated Title by Integration Test"}
    updated_experiment = labguru_api.update_experiment(experiment_id, update_fields)
    assert updated_experiment.get("title") == update_fields["title"], "Experiment title was not updated."

    # Revert to original
    revert_fields = {"title": original_title}
    reverted_experiment = labguru_api.update_experiment(experiment_id, revert_fields)
    assert reverted_experiment.get("title") == original_title, "Experiment title was not reverted."


@pytest.mark.integration
def test_create_and_delete_experiment(labguru_api):
    payload = test_settings.CREATE_EXPERIMENT_PAYLOAD
    created_experiment = labguru_api.create_experiment(experiment_data=payload)
    assert "id" in created_experiment, "Created experiment does not have an 'id'."
    experiment_id = created_experiment["id"]

    retrieved_experiment = labguru_api.get_experiment_by_id(experiment_id)
    assert retrieved_experiment.get("title") == payload["title"], "Experiment title does not match."

    labguru_api.delete_experiment(experiment_id)
    with pytest.raises(Exception):
        labguru_api.get_experiment_by_id(experiment_id)
