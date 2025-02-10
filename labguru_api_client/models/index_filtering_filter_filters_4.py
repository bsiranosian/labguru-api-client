from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_filtering_filter_filters_4_value import IndexFilteringFilterFilters4Value


T = TypeVar("T", bound="IndexFilteringFilterFilters4")


@_attrs_define
class IndexFilteringFilterFilters4:
    """Filter object

    Attributes:
        field (Union[Unset, str]): Field name to filter by Example: stored_by.
        operator (Union[Unset, str]): Filter operator (e.g., "contains") Example: contains.
        value (Union[Unset, IndexFilteringFilterFilters4Value]):
    """

    field: Union[Unset, str] = UNSET
    operator: Union[Unset, str] = UNSET
    value: Union[Unset, "IndexFilteringFilterFilters4Value"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator = self.operator

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

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
        from ..models.index_filtering_filter_filters_4_value import IndexFilteringFilterFilters4Value

        d = src_dict.copy()
        field = d.pop("field", UNSET)

        operator = d.pop("operator", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, IndexFilteringFilterFilters4Value]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IndexFilteringFilterFilters4Value.from_dict(_value)

        index_filtering_filter_filters_4 = cls(
            field=field,
            operator=operator,
            value=value,
        )

        index_filtering_filter_filters_4.additional_properties = d
        return index_filtering_filter_filters_4

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
