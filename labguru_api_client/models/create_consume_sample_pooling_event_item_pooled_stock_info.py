from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateConsumeSamplePoolingEventItemPooledStockInfo")


@_attrs_define
class CreateConsumeSamplePoolingEventItemPooledStockInfo:
    """Contains all the necessary stock fields for creating a stock during the pooling event.
                    This object may include all the relevant stock properties.

    Attributes:
        stockable_type (str): Identifies the class name of the stock item, such as 'Biocollections::Bacterium'.
                                  This indicates the category of the entity and must match valid system-defined class names.
            Example: Biocollections::Bacterium.
        stockable_id (int):
        storage_type (str): Specifies the storage classification, such as 'System::Storage::Storage', indicating the
            type of storage facility used for the item. Example: System::Storage::Storage.
        storage_id (int):
        name (str):
    """

    stockable_type: str
    stockable_id: int
    storage_type: str
    storage_id: int
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stockable_type = self.stockable_type

        stockable_id = self.stockable_id

        storage_type = self.storage_type

        storage_id = self.storage_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stockable_type": stockable_type,
                "stockable_id": stockable_id,
                "storage_type": storage_type,
                "storage_id": storage_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        stockable_type = d.pop("stockable_type")

        stockable_id = d.pop("stockable_id")

        storage_type = d.pop("storage_type")

        storage_id = d.pop("storage_id")

        name = d.pop("name")

        create_consume_sample_pooling_event_item_pooled_stock_info = cls(
            stockable_type=stockable_type,
            stockable_id=stockable_id,
            storage_type=storage_type,
            storage_id=storage_id,
            name=name,
        )

        create_consume_sample_pooling_event_item_pooled_stock_info.additional_properties = d
        return create_consume_sample_pooling_event_item_pooled_stock_info

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
