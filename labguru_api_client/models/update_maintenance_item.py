from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMaintenanceItem")


@_attrs_define
class UpdateMaintenanceItem:
    """
    Attributes:
        item_id (int): the id of the equipment Example: The equipment id.
        frequency_period (Union[Unset, int]): the time period in numbers Example: 15.
        frequency_frame (Union[Unset, str]): one of the following time frames - hour/day/week/month/year Example: day.
    """

    item_id: int
    frequency_period: Union[Unset, int] = UNSET
    frequency_frame: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        frequency_period = self.frequency_period

        frequency_frame = self.frequency_frame

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
            }
        )
        if frequency_period is not UNSET:
            field_dict["frequency_period"] = frequency_period
        if frequency_frame is not UNSET:
            field_dict["frequency_frame"] = frequency_frame

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("item_id")

        frequency_period = d.pop("frequency_period", UNSET)

        frequency_frame = d.pop("frequency_frame", UNSET)

        update_maintenance_item = cls(
            item_id=item_id,
            frequency_period=frequency_period,
            frequency_frame=frequency_frame,
        )

        update_maintenance_item.additional_properties = d
        return update_maintenance_item

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
