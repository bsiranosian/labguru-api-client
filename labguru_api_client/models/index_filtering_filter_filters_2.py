import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexFilteringFilterFilters2")


@_attrs_define
class IndexFilteringFilterFilters2:
    """Filter object

    Attributes:
        field (Union[Unset, str]): Field name to filter by Example: stored_on.
        operator (Union[Unset, str]): Filter operator (e.g., "_gt") Example: _gt.
        value (Union[Unset, datetime.date]): Filter value - Date in the following format 'YYYY-MM-DD' Example:
            2023-01-11.
    """

    field: Union[Unset, str] = UNSET
    operator: Union[Unset, str] = UNSET
    value: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator = self.operator

        value: Union[Unset, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field", UNSET)

        operator = d.pop("operator", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, datetime.date]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = isoparse(_value).date()

        index_filtering_filter_filters_2 = cls(
            field=field,
            operator=operator,
            value=value,
        )

        index_filtering_filter_filters_2.additional_properties = d
        return index_filtering_filter_filters_2

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
