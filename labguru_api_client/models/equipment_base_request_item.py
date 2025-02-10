from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EquipmentBaseRequestItem")


@_attrs_define
class EquipmentBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): the company name Example: company name.
        model_number (Union[Unset, str]): model number of the equipment Example: EQ-123.
        serial_number (Union[Unset, str]): serial number of the equipment  Example: SE-12.
        equipment_type (Union[Unset, str]): equipment type  Example: type A.
        manufacturer (Union[Unset, str]): manufacturer name  Example: companyName inc..
        purchase_date (Union[Unset, str]): purchase date  Example: yyyy-mm-dd.
        warranty_expired (Union[Unset, str]): warranty_expired  Example: yyyy-mm-dd.
        maintenance_information (Union[Unset, str]): maintenance information  Example: general maintenance info.
        description (Union[Unset, str]): general description  Example: general description of the equipment.
    """

    name: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    equipment_type: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, str] = UNSET
    warranty_expired: Union[Unset, str] = UNSET
    maintenance_information: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        model_number = self.model_number

        serial_number = self.serial_number

        equipment_type = self.equipment_type

        manufacturer = self.manufacturer

        purchase_date = self.purchase_date

        warranty_expired = self.warranty_expired

        maintenance_information = self.maintenance_information

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if model_number is not UNSET:
            field_dict["model_number"] = model_number
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if equipment_type is not UNSET:
            field_dict["equipment_type"] = equipment_type
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date
        if warranty_expired is not UNSET:
            field_dict["warranty_expired"] = warranty_expired
        if maintenance_information is not UNSET:
            field_dict["maintenance_information"] = maintenance_information
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        model_number = d.pop("model_number", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        equipment_type = d.pop("equipment_type", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        purchase_date = d.pop("purchase_date", UNSET)

        warranty_expired = d.pop("warranty_expired", UNSET)

        maintenance_information = d.pop("maintenance_information", UNSET)

        description = d.pop("description", UNSET)

        equipment_base_request_item = cls(
            name=name,
            model_number=model_number,
            serial_number=serial_number,
            equipment_type=equipment_type,
            manufacturer=manufacturer,
            purchase_date=purchase_date,
            warranty_expired=warranty_expired,
            maintenance_information=maintenance_information,
            description=description,
        )

        equipment_base_request_item.additional_properties = d
        return equipment_base_request_item

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
