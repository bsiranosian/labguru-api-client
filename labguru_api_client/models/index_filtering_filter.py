from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_filtering_filter_filters import IndexFilteringFilterFilters


T = TypeVar("T", bound="IndexFilteringFilter")


@_attrs_define
class IndexFilteringFilter:
    """
    Attributes:
        logic (Union[Unset, str]): Filter logic (e.g., "and" or "or") Example: and.
        filters (Union[Unset, IndexFilteringFilterFilters]): Array of filter objects
    """

    logic: Union[Unset, str] = UNSET
    filters: Union[Unset, "IndexFilteringFilterFilters"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logic = self.logic

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logic is not UNSET:
            field_dict["logic"] = logic
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.index_filtering_filter_filters import IndexFilteringFilterFilters

        d = src_dict.copy()
        logic = d.pop("logic", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, IndexFilteringFilterFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = IndexFilteringFilterFilters.from_dict(_filters)

        index_filtering_filter = cls(
            logic=logic,
            filters=filters,
        )

        index_filtering_filter.additional_properties = d
        return index_filtering_filter

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
