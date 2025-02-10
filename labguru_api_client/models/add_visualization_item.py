from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddVisualizationItem")


@_attrs_define
class AddVisualizationItem:
    """
    Attributes:
        name (str): The name of the visualization Example: Temperature trends.
        dataset_id (int): The ID of the dataset to which the visualization will be linked to Example: 13.
        attachment_id (int): The ID of the attachment (image) that will appear under the 'Visualization' tab of the
            dataset Example: 203.
    """

    name: str
    dataset_id: int
    attachment_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        dataset_id = self.dataset_id

        attachment_id = self.attachment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dataset_id": dataset_id,
                "attachment_id": attachment_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        dataset_id = d.pop("dataset_id")

        attachment_id = d.pop("attachment_id")

        add_visualization_item = cls(
            name=name,
            dataset_id=dataset_id,
            attachment_id=attachment_id,
        )

        add_visualization_item.additional_properties = d
        return add_visualization_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
