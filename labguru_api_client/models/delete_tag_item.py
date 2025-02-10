from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteTagItem")


@_attrs_define
class DeleteTagItem:
    """
    Attributes:
        tag (str): the tag name to remove  Example: Restricted.
        class_name (str): the item type to remove the tag from Example: Biocollections::Antibody.
        item_id (str): the id of the item to to remove the tag from Example: 1.
    """

    tag: str
    class_name: str
    item_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag

        class_name = self.class_name

        item_id = self.item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
                "class_name": class_name,
                "item_id": item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = d.pop("tag")

        class_name = d.pop("class_name")

        item_id = d.pop("item_id")

        delete_tag_item = cls(
            tag=tag,
            class_name=class_name,
            item_id=item_id,
        )

        delete_tag_item.additional_properties = d
        return delete_tag_item

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
