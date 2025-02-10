from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCustomSamplePoolingEventItemStocksUsage")


@_attrs_define
class CreateCustomSamplePoolingEventItemStocksUsage:
    """Hash of stock IDs and the desired amount to pool.

    Example:
        {'300': 0.004, '834': 6, '45': 5}

    """

    additional_properties: dict[str, float] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        create_custom_sample_pooling_event_item_stocks_usage = cls()

        create_custom_sample_pooling_event_item_stocks_usage.additional_properties = d
        return create_custom_sample_pooling_event_item_stocks_usage

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> float:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: float) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
