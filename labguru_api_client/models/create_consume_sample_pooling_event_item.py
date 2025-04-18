from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_consume_sample_pooling_event_item_pooled_stock_info import (
        CreateConsumeSamplePoolingEventItemPooledStockInfo,
    )


T = TypeVar("T", bound="CreateConsumeSamplePoolingEventItem")


@_attrs_define
class CreateConsumeSamplePoolingEventItem:
    """
    Attributes:
        name (str): The description of pool purpose
        unit_type (str): volume/weight
        pool_type (str):  Example: consume.
        unit (str): Valid units of measurement are:

            - For 'volume': 'nL', 'µL', 'mL', 'L'
            - For 'weight': 'ng', 'µg', 'mg', 'g', 'Kg' Example: µL.
        stocks_list (list[int]): List of stock IDs from which to draw Example: [1291, 1293].
        pooled_stock_info (CreateConsumeSamplePoolingEventItemPooledStockInfo): Contains all the necessary stock fields
            for creating a stock during the pooling event.
                                This object may include all the relevant stock properties.
    """

    name: str
    unit_type: str
    pool_type: str
    unit: str
    stocks_list: list[int]
    pooled_stock_info: "CreateConsumeSamplePoolingEventItemPooledStockInfo"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        unit_type = self.unit_type

        pool_type = self.pool_type

        unit = self.unit

        stocks_list = self.stocks_list

        pooled_stock_info = self.pooled_stock_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "unit_type": unit_type,
                "pool_type": pool_type,
                "unit": unit,
                "stocks_list": stocks_list,
                "pooled_stock_info": pooled_stock_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_consume_sample_pooling_event_item_pooled_stock_info import (
            CreateConsumeSamplePoolingEventItemPooledStockInfo,
        )

        d = src_dict.copy()
        name = d.pop("name")

        unit_type = d.pop("unit_type")

        pool_type = d.pop("pool_type")

        unit = d.pop("unit")

        stocks_list = cast(list[int], d.pop("stocks_list"))

        pooled_stock_info = CreateConsumeSamplePoolingEventItemPooledStockInfo.from_dict(d.pop("pooled_stock_info"))

        create_consume_sample_pooling_event_item = cls(
            name=name,
            unit_type=unit_type,
            pool_type=pool_type,
            unit=unit,
            stocks_list=stocks_list,
            pooled_stock_info=pooled_stock_info,
        )

        create_consume_sample_pooling_event_item.additional_properties = d
        return create_consume_sample_pooling_event_item

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
