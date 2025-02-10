from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateOrderItem")


@_attrs_define
class UpdateOrderItem:
    """
    Attributes:
        price (Union[Unset, float]): price Example: 20.6.
        budget (Union[Unset, str]): budget Example: 1000.
        currency (Union[Unset, int]): 0 = NIS, 1 = DOLLAR, 2 = EURO, 3 = POUND, 4 = NOK  Example: 1.
        quantity (Union[Unset, int]): quantity Example: 5.
        order_number (Union[Unset, int]): order number Example: 3.
        description (Union[Unset, str]): description Example: general description.
    """

    price: Union[Unset, float] = UNSET
    budget: Union[Unset, str] = UNSET
    currency: Union[Unset, int] = UNSET
    quantity: Union[Unset, int] = UNSET
    order_number: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        budget = self.budget

        currency = self.currency

        quantity = self.quantity

        order_number = self.order_number

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if budget is not UNSET:
            field_dict["budget"] = budget
        if currency is not UNSET:
            field_dict["currency"] = currency
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if order_number is not UNSET:
            field_dict["order_number"] = order_number
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        price = d.pop("price", UNSET)

        budget = d.pop("budget", UNSET)

        currency = d.pop("currency", UNSET)

        quantity = d.pop("quantity", UNSET)

        order_number = d.pop("order_number", UNSET)

        description = d.pop("description", UNSET)

        update_order_item = cls(
            price=price,
            budget=budget,
            currency=currency,
            quantity=quantity,
            order_number=order_number,
            description=description,
        )

        update_order_item.additional_properties = d
        return update_order_item

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
