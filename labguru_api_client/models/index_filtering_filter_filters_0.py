from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexFilteringFilterFilters0")


@_attrs_define
class IndexFilteringFilterFilters0:
    """Filter object

    Attributes:
        field (Union[Unset, str]): Field name to filter by Example: name.
        operator (Union[Unset, str]): Filter operator (e.g., "contains") Example: contains.
        value (Union[Unset, str]): Filter value Example: myValue.
    """

    field: Union[Unset, str] = UNSET
    operator: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator = self.operator

        value = self.value

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

        value = d.pop("value", UNSET)

        index_filtering_filter_filters_0 = cls(
            field=field,
            operator=operator,
            value=value,
        )

        index_filtering_filter_filters_0.additional_properties = d
        return index_filtering_filter_filters_0

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
