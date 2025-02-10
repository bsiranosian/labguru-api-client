from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_filtering_filter_filters_0 import IndexFilteringFilterFilters0
    from ..models.index_filtering_filter_filters_1 import IndexFilteringFilterFilters1
    from ..models.index_filtering_filter_filters_2 import IndexFilteringFilterFilters2
    from ..models.index_filtering_filter_filters_3 import IndexFilteringFilterFilters3
    from ..models.index_filtering_filter_filters_4 import IndexFilteringFilterFilters4


T = TypeVar("T", bound="IndexFilteringFilterFilters")


@_attrs_define
class IndexFilteringFilterFilters:
    """Array of filter objects

    Attributes:
        field_0 (Union[Unset, IndexFilteringFilterFilters0]): Filter object
        field_1 (Union[Unset, IndexFilteringFilterFilters1]): Filter object
        field_2 (Union[Unset, IndexFilteringFilterFilters2]): Filter object
        field_3 (Union[Unset, IndexFilteringFilterFilters3]): Filter object
        field_4 (Union[Unset, IndexFilteringFilterFilters4]): Filter object
    """

    field_0: Union[Unset, "IndexFilteringFilterFilters0"] = UNSET
    field_1: Union[Unset, "IndexFilteringFilterFilters1"] = UNSET
    field_2: Union[Unset, "IndexFilteringFilterFilters2"] = UNSET
    field_3: Union[Unset, "IndexFilteringFilterFilters3"] = UNSET
    field_4: Union[Unset, "IndexFilteringFilterFilters4"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_0: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_0, Unset):
            field_0 = self.field_0.to_dict()

        field_1: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_1, Unset):
            field_1 = self.field_1.to_dict()

        field_2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_2, Unset):
            field_2 = self.field_2.to_dict()

        field_3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_3, Unset):
            field_3 = self.field_3.to_dict()

        field_4: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_4, Unset):
            field_4 = self.field_4.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_0 is not UNSET:
            field_dict["0"] = field_0
        if field_1 is not UNSET:
            field_dict["1"] = field_1
        if field_2 is not UNSET:
            field_dict["2"] = field_2
        if field_3 is not UNSET:
            field_dict["3"] = field_3
        if field_4 is not UNSET:
            field_dict["4"] = field_4

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.index_filtering_filter_filters_0 import IndexFilteringFilterFilters0
        from ..models.index_filtering_filter_filters_1 import IndexFilteringFilterFilters1
        from ..models.index_filtering_filter_filters_2 import IndexFilteringFilterFilters2
        from ..models.index_filtering_filter_filters_3 import IndexFilteringFilterFilters3
        from ..models.index_filtering_filter_filters_4 import IndexFilteringFilterFilters4

        d = src_dict.copy()
        _field_0 = d.pop("0", UNSET)
        field_0: Union[Unset, IndexFilteringFilterFilters0]
        if isinstance(_field_0, Unset):
            field_0 = UNSET
        else:
            field_0 = IndexFilteringFilterFilters0.from_dict(_field_0)

        _field_1 = d.pop("1", UNSET)
        field_1: Union[Unset, IndexFilteringFilterFilters1]
        if isinstance(_field_1, Unset):
            field_1 = UNSET
        else:
            field_1 = IndexFilteringFilterFilters1.from_dict(_field_1)

        _field_2 = d.pop("2", UNSET)
        field_2: Union[Unset, IndexFilteringFilterFilters2]
        if isinstance(_field_2, Unset):
            field_2 = UNSET
        else:
            field_2 = IndexFilteringFilterFilters2.from_dict(_field_2)

        _field_3 = d.pop("3", UNSET)
        field_3: Union[Unset, IndexFilteringFilterFilters3]
        if isinstance(_field_3, Unset):
            field_3 = UNSET
        else:
            field_3 = IndexFilteringFilterFilters3.from_dict(_field_3)

        _field_4 = d.pop("4", UNSET)
        field_4: Union[Unset, IndexFilteringFilterFilters4]
        if isinstance(_field_4, Unset):
            field_4 = UNSET
        else:
            field_4 = IndexFilteringFilterFilters4.from_dict(_field_4)

        index_filtering_filter_filters = cls(
            field_0=field_0,
            field_1=field_1,
            field_2=field_2,
            field_3=field_3,
            field_4=field_4,
        )

        index_filtering_filter_filters.additional_properties = d
        return index_filtering_filter_filters

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
