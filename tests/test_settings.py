# List of project, milestone, experiment, etc IDs for use in read-only tests
ALLOWED_PROJECT_IDS = [8]
ALLOWED_FOLDER_IDS = [105]
ALLOWED_EXPERIMENT_IDS = [402]
ALLOWED_PLASMID_IDS = [402]


# One experiment that can be modified by the integration tests.
PROJECT_TO_MODIFY = 8
FOLDER_TO_MODIFY = 105
EXPERIMENT_TO_MODIFY = 402
PLASMID_TO_MODIFY = 2063

# Payload templates
CREATE_EXPERIMENT_PAYLOAD = {"title": "Integration Test Experiment", "project_id": PROJECT_TO_MODIFY, "milestone_id": FOLDER_TO_MODIFY}
CREATE_FOLDER_PAYLOAD = {"title": "Integration Test Folder", "project_id": PROJECT_TO_MODIFY}
CREATE_ATTACHMENT_PAYLOAD = {"description": "Integration Test Attachment"}
CREATE_PROJECT_PAYLOAD = {"title": "Integration Test Project"}
CREATE_PLASMID_PAYLOAD = {"title": "Integration Test Plasmid", "PLM number": -666}

# biocollections settings
TEST_GENERIC_COLLECTION_NAME = "test_collection"
GENERIC_COLLECTION_FILTER_VALUE = "_1"
CREATE_GENERIC_ITEM_PAYLOAD = {"name": "Integration Test Item", "test_field": "123"}
