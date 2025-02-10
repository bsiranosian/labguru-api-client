from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDatasetItem")


@_attrs_define
class CreateDatasetItem:
    """
    Attributes:
        name (str): dataset name Example: Dataset 123.
        data_attachment_id (int): dataset attachment id Example: 4.
        sdf_attachment_id (Union[Unset, int]): SDF attachment id Example: 5.
        description (Union[Unset, str]): dataset description Example: RuBisCO large subunit.
    """

    name: str
    data_attachment_id: int
    sdf_attachment_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data_attachment_id = self.data_attachment_id

        sdf_attachment_id = self.sdf_attachment_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "data_attachment_id": data_attachment_id,
            }
        )
        if sdf_attachment_id is not UNSET:
            field_dict["sdf_attachment_id"] = sdf_attachment_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        data_attachment_id = d.pop("data_attachment_id")

        sdf_attachment_id = d.pop("sdf_attachment_id", UNSET)

        description = d.pop("description", UNSET)

        create_dataset_item = cls(
            name=name,
            data_attachment_id=data_attachment_id,
            sdf_attachment_id=sdf_attachment_id,
            description=description,
        )

        create_dataset_item.additional_properties = d
        return create_dataset_item

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
