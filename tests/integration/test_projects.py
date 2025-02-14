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
def test_get_all_projects(labguru_api):
    projects = labguru_api.get_all_projects(page=1, meta="false")
    assert isinstance(projects, (dict, list)), "Response should be a dict or list."


@pytest.mark.integration
def test_get_project(labguru_api):
    project_id = test_settings.PROJECT_TO_MODIFY
    project = labguru_api.get_project(project_id)
    assert project.get("id") == project_id, f"Retrieved project id {project.get('id')} does not match expected {project_id}."


@pytest.mark.integration
def test_update_project(labguru_api):
    project_id = test_settings.PROJECT_TO_MODIFY
    original_project = labguru_api.get_project(project_id)
    original_title = original_project.get("title")
    update_fields = {"title": "Updated Project Title by Integration Test"}
    updated_project = labguru_api.update_project(project_id, update_fields)
    assert updated_project.get("title") == update_fields["title"], "Project title was not updated."

    # Revert to original
    revert_fields = {"title": original_title}
    reverted_project = labguru_api.update_project(project_id, revert_fields)
    assert reverted_project.get("title") == original_title, "Project title was not reverted."


@pytest.mark.skip(reason="Delete project not supported by the Labguru API")
@pytest.mark.integration
def test_create_and_delete_project(labguru_api):
    payload = test_settings.CREATE_PROJECT_PAYLOAD
    created_project = labguru_api.create_project(project_data=payload)
    assert "id" in created_project, "Created project does not have an 'id'."
    project_id = created_project["id"]

    retrieved_project = labguru_api.get_project(project_id)
    assert retrieved_project.get("title") == payload["title"], "Project title does not match."

    labguru_api.delete_project(project_id)
    with pytest.raises(Exception):
        labguru_api.get_project(project_id)
