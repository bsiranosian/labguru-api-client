from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateMaintenanceItem")


@_attrs_define
class CreateMaintenanceItem:
    """
    Attributes:
        item_id (int): the id of the equipment Example: The equipment id.
        item_type (str): the class of the item (System::Instrument) Example: System::Instrument.
        maintenance_type_id (int): the id of the maintanance type Example: The maintenance type id.
        frequency_period (int): the time period in numbers Example: 1.
        frequency_frame (str): one of the following time frames - hour/day/week/month/year Example: year.
    """

    item_id: int
    item_type: str
    maintenance_type_id: int
    frequency_period: int
    frequency_frame: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        item_type = self.item_type

        maintenance_type_id = self.maintenance_type_id

        frequency_period = self.frequency_period

        frequency_frame = self.frequency_frame

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "item_type": item_type,
                "maintenance_type_id": maintenance_type_id,
                "frequency_period": frequency_period,
                "frequency_frame": frequency_frame,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("item_id")

        item_type = d.pop("item_type")

        maintenance_type_id = d.pop("maintenance_type_id")

        frequency_period = d.pop("frequency_period")

        frequency_frame = d.pop("frequency_frame")

        create_maintenance_item = cls(
            item_id=item_id,
            item_type=item_type,
            maintenance_type_id=maintenance_type_id,
            frequency_period=frequency_period,
            frequency_frame=frequency_frame,
        )

        create_maintenance_item.additional_properties = d
        return create_maintenance_item

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
