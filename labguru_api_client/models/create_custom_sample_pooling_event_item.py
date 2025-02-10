from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_custom_sample_pooling_event_item_pooled_stock_info import (
        CreateCustomSamplePoolingEventItemPooledStockInfo,
    )
    from ..models.create_custom_sample_pooling_event_item_stocks_usage import (
        CreateCustomSamplePoolingEventItemStocksUsage,
    )


T = TypeVar("T", bound="CreateCustomSamplePoolingEventItem")


@_attrs_define
class CreateCustomSamplePoolingEventItem:
    """
    Attributes:
        name (str): The description of pool purpose
        unit_type (str): volume/weight
        pool_type (str):  Example: custom.
        unit (str): Valid units of measurement are:

            - For 'volume': 'nL', 'µL', 'mL', 'L'
            - For 'weight': 'ng', 'µg', 'mg', 'g', 'Kg' Example: µL.
        stocks_usage (CreateCustomSamplePoolingEventItemStocksUsage): Hash of stock IDs and the desired amount to pool.
            Example: {'300': 0.004, '834': 6, '45': 5}.
        pooled_stock_info (CreateCustomSamplePoolingEventItemPooledStockInfo): Contains all the necessary stock fields
            for creating a stock during the pooling event.
                                This object may include all the relevant stock properties.
    """

    name: str
    unit_type: str
    pool_type: str
    unit: str
    stocks_usage: "CreateCustomSamplePoolingEventItemStocksUsage"
    pooled_stock_info: "CreateCustomSamplePoolingEventItemPooledStockInfo"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        unit_type = self.unit_type

        pool_type = self.pool_type

        unit = self.unit

        stocks_usage = self.stocks_usage.to_dict()

        pooled_stock_info = self.pooled_stock_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "unit_type": unit_type,
                "pool_type": pool_type,
                "unit": unit,
                "stocks_usage": stocks_usage,
                "pooled_stock_info": pooled_stock_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_custom_sample_pooling_event_item_pooled_stock_info import (
            CreateCustomSamplePoolingEventItemPooledStockInfo,
        )
        from ..models.create_custom_sample_pooling_event_item_stocks_usage import (
            CreateCustomSamplePoolingEventItemStocksUsage,
        )

        d = src_dict.copy()
        name = d.pop("name")

        unit_type = d.pop("unit_type")

        pool_type = d.pop("pool_type")

        unit = d.pop("unit")

        stocks_usage = CreateCustomSamplePoolingEventItemStocksUsage.from_dict(d.pop("stocks_usage"))

        pooled_stock_info = CreateCustomSamplePoolingEventItemPooledStockInfo.from_dict(d.pop("pooled_stock_info"))

        create_custom_sample_pooling_event_item = cls(
            name=name,
            unit_type=unit_type,
            pool_type=pool_type,
            unit=unit,
            stocks_usage=stocks_usage,
            pooled_stock_info=pooled_stock_info,
        )

        create_custom_sample_pooling_event_item.additional_properties = d
        return create_custom_sample_pooling_event_item

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
