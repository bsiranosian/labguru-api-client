import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceEventBaseRequestItem")


@_attrs_define
class MaintenanceEventBaseRequestItem:
    """
    Attributes:
        item_id (Union[Unset, int]): the equipment id Example: 1.
        item_type (Union[Unset, str]): equipment class name Example: System::Instrument.
        maintenance_id (Union[Unset, int]): maintenance id Example: 2.
        data (Union[Unset, str]): templates fields in the follwing json format Example:
            [{"title":"Detergent","value":"Wateriii:"}].
        performed_at (Union[Unset, datetime.date]): performance data Example: Jun 10, 2021 11:51.
        performed_by (Union[Unset, int]): member id Example: 9.
    """

    item_id: Union[Unset, int] = UNSET
    item_type: Union[Unset, str] = UNSET
    maintenance_id: Union[Unset, int] = UNSET
    data: Union[Unset, str] = UNSET
    performed_at: Union[Unset, datetime.date] = UNSET
    performed_by: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        item_type = self.item_type

        maintenance_id = self.maintenance_id

        data = self.data

        performed_at: Union[Unset, str] = UNSET
        if not isinstance(self.performed_at, Unset):
            performed_at = self.performed_at.isoformat()

        performed_by = self.performed_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if maintenance_id is not UNSET:
            field_dict["maintenance_id"] = maintenance_id
        if data is not UNSET:
            field_dict["data"] = data
        if performed_at is not UNSET:
            field_dict["performed_at"] = performed_at
        if performed_by is not UNSET:
            field_dict["performed_by"] = performed_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("item_id", UNSET)

        item_type = d.pop("item_type", UNSET)

        maintenance_id = d.pop("maintenance_id", UNSET)

        data = d.pop("data", UNSET)

        _performed_at = d.pop("performed_at", UNSET)
        performed_at: Union[Unset, datetime.date]
        if isinstance(_performed_at, Unset):
            performed_at = UNSET
        else:
            performed_at = isoparse(_performed_at).date()

        performed_by = d.pop("performed_by", UNSET)

        maintenance_event_base_request_item = cls(
            item_id=item_id,
            item_type=item_type,
            maintenance_id=maintenance_id,
            data=data,
            performed_at=performed_at,
            performed_by=performed_by,
        )

        maintenance_event_base_request_item.additional_properties = d
        return maintenance_event_base_request_item

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
