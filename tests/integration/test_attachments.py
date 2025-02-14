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
def test_upload_and_get_attachment(labguru_api, tmp_path):
    # Create a temporary file to simulate an attachment.
    file_content = "This is a test attachment."
    file_path = tmp_path / "test_attachment.txt"
    file_path.write_text(file_content)

    attachment_data = test_settings.CREATE_ATTACHMENT_PAYLOAD
    created_attachment = labguru_api.upload_attachment(file_path=file_path, description=attachment_data.get("description"))

    assert "id" in created_attachment, "Created attachment does not have an 'id'."
    attachment_id = created_attachment["id"]

    retrieved_attachment = labguru_api.get_attachment(attachment_id)
    expected_desc = attachment_data.get("description", "")
    assert retrieved_attachment.get("description") == expected_desc, "Attachment description does not match."

    labguru_api.delete_attachment(attachment_id)
    # seems like attachments are not currenly deleted, even if the DELETE request is successful
    # with pytest.raises(Exception):
    #     labguru_api.get_attachment(attachment_id)


# TODO: Link attachment to an element (the PUT/update request)
