from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignItemToDatasetItem")


@_attrs_define
class AssignItemToDatasetItem:
    """
    Attributes:
        item_type (str): the item type to attach the dataset to Example: Element.
        item_id (int): the id of the item Example: 4.
    """

    item_type: str
    item_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type

        item_id = self.item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_type": item_type,
                "item_id": item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        item_type = d.pop("item_type")

        item_id = d.pop("item_id")

        assign_item_to_dataset_item = cls(
            item_type=item_type,
            item_id=item_id,
        )

        assign_item_to_dataset_item.additional_properties = d
        return assign_item_to_dataset_item

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
