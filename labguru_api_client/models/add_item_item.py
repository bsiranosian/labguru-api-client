from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddItemItem")


@_attrs_define
class AddItemItem:
    """
    Attributes:
        collection_type (str): The type of collection, specified in singular form. Example: Biocollections::Antibody.
        item_id (int): The id of the item to be added to the shopping list Example: 423.
        quantity (int): The number of units of the item to be added to the shopping list. Example: 5.
        price (Union[Unset, float]): The price of the item Example: 20.6.
        currency (Union[Unset, int]):  Example: 1.
        remarks (Union[Unset, str]): Additional comments or special instructions related to the item. Example: Please
            deliver between 9 AM and 12 PM..
    """

    collection_type: str
    item_id: int
    quantity: int
    price: Union[Unset, float] = UNSET
    currency: Union[Unset, int] = UNSET
    remarks: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_type = self.collection_type

        item_id = self.item_id

        quantity = self.quantity

        price = self.price

        currency = self.currency

        remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_type": collection_type,
                "item_id": item_id,
                "quantity": quantity,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_type = d.pop("collection_type")

        item_id = d.pop("item_id")

        quantity = d.pop("quantity")

        price = d.pop("price", UNSET)

        currency = d.pop("currency", UNSET)

        remarks = d.pop("remarks", UNSET)

        add_item_item = cls(
            collection_type=collection_type,
            item_id=item_id,
            quantity=quantity,
            price=price,
            currency=currency,
            remarks=remarks,
        )

        add_item_item.additional_properties = d
        return add_item_item

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
