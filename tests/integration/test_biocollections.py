import os
import pytest
import pandas as pd
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
def test_filter_biocollection_items(labguru_api):
    """
    Test filtering custom collection items.
    """
    # Use test settings for collection name and filter values.
    collection_name = test_settings.TEST_GENERIC_COLLECTION_NAME
    filter_field = "title"
    filter_operator = "contains"
    filter_value = test_settings.GENERIC_COLLECTION_FILTER_VALUE  # some filter term from test settings

    response = labguru_api.filter_biocollection_items(
        collection_name=collection_name,
        filter_field=filter_field,
        filter_operator=filter_operator,
        filter_value=filter_value,
        page=1,
        meta="true",
        kendo="true",
        filter_logic="and",
    )
    assert isinstance(response, dict), "Response should be a dict."
    assert "meta" in response, "Response should have a 'meta' key."
    assert "data" in response, "Response should have a 'data' key."
    assert isinstance(response["data"], list), "Response data should be a list."


@pytest.mark.integration
def test_list_generic_items(labguru_api):
    """
    Test listing generic items in a collection.
    """
    generic_collection_name = test_settings.TEST_GENERIC_COLLECTION_NAME
    response = labguru_api.list_generic_items(
        generic_collection_name=generic_collection_name,
        page=1,
        meta="true",
    )
    assert isinstance(response, dict), "Response should be a dict."
    assert "meta" in response, "Response should have a 'meta' key."
    assert "data" in response, "Response should have a 'data' key."
    assert isinstance(response["data"], list), "Response data should be a list."


@pytest.mark.integration
def test_list_generic_items_all_pages(labguru_api):
    """
    Test listing generic items in a collection.
    """
    generic_collection_name = test_settings.TEST_GENERIC_COLLECTION_NAME
    response = labguru_api.list_generic_items_all_pages(
        generic_collection_name=generic_collection_name,
    )
    assert isinstance(response, list), "Response should be a list."
    assert isinstance(response[0], dict), "Response data should be a list of dict."


@pytest.mark.integration
def test_collection_to_df(labguru_api):
    """
    Test getting a dataframe from a collection
    """
    generic_collection_name = test_settings.TEST_GENERIC_COLLECTION_NAME
    df = labguru_api.collection_to_df(generic_collection_name)
    assert isinstance(df, pd.DataFrame), "Response should be a pandas DataFrame."
    assert df.shape[0] > 0, "Dataframe should have at least one row."


@pytest.mark.integration
def test_create_and_update_generic_item(labguru_api):
    """
    Test creating a generic item and then updating it.
    """
    generic_collection_name = test_settings.TEST_GENERIC_COLLECTION_NAME

    # Create a new generic item using a payload from test settings.
    create_payload = test_settings.CREATE_GENERIC_ITEM_PAYLOAD
    created_item = labguru_api.create_generic_item(generic_collection_name, create_payload)
    assert "id" in created_item, "Created generic item does not have an 'id'."
    generic_item_id = created_item["id"]

    # Update the generic item.
    update_fields = {"name": "Updated Name by Integration Test"}
    updated_item = labguru_api.update_generic_item(generic_collection_name, generic_item_id, update_fields)
    assert updated_item.get("name") == update_fields["name"], "Generic item name was not updated."

    # delete the created item
    labguru_api.delete_generic_item(generic_collection_name, generic_item_id)
    with pytest.raises(Exception):
        labguru_api.get_generic_item(generic_collection_name, generic_item_id)
