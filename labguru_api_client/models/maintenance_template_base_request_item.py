from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceTemplateBaseRequestItem")


@_attrs_define
class MaintenanceTemplateBaseRequestItem:
    """
    Attributes:
        equipment_type (Union[Unset, str]): the equipment type Example: Centrifuges.
        maintenance_type_id (Union[Unset, int]): maintenance type id Example: EQ-123.
        data (Union[Unset, str]): templates fields in the follwing json format Example:
            [{"title":"Detergent","value":"Wateriii:"}].
    """

    equipment_type: Union[Unset, str] = UNSET
    maintenance_type_id: Union[Unset, int] = UNSET
    data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        equipment_type = self.equipment_type

        maintenance_type_id = self.maintenance_type_id

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if equipment_type is not UNSET:
            field_dict["equipment_type"] = equipment_type
        if maintenance_type_id is not UNSET:
            field_dict["maintenance_type_id"] = maintenance_type_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        equipment_type = d.pop("equipment_type", UNSET)

        maintenance_type_id = d.pop("maintenance_type_id", UNSET)

        data = d.pop("data", UNSET)

        maintenance_template_base_request_item = cls(
            equipment_type=equipment_type,
            maintenance_type_id=maintenance_type_id,
            data=data,
        )

        maintenance_template_base_request_item.additional_properties = d
        return maintenance_template_base_request_item

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
