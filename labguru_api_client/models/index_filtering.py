from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_filtering_filter import IndexFilteringFilter


T = TypeVar("T", bound="IndexFiltering")


@_attrs_define
class IndexFiltering:
    """
    Attributes:
        kendo (str):  Example: true.
        filter_ (Union[Unset, IndexFilteringFilter]):
    """

    kendo: str
    filter_: Union[Unset, "IndexFilteringFilter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kendo = self.kendo

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kendo": kendo,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.index_filtering_filter import IndexFilteringFilter

        d = src_dict.copy()
        kendo = d.pop("kendo")

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, IndexFilteringFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = IndexFilteringFilter.from_dict(_filter_)

        index_filtering = cls(
            kendo=kendo,
            filter_=filter_,
        )

        index_filtering.additional_properties = d
        return index_filtering

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
