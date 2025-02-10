from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1PoolEventsResponse200")


@_attrs_define
class PostApiV1PoolEventsResponse200:
    """Returns detailed information about the updated pool event.

    Attributes:
        id (Union[Unset, int]): The ID of the pool event Example: 7.
        name (Union[Unset, str]): The description of pool purpose
        unit_type (Union[Unset, str]):  Example: volume.
        pool_type (Union[Unset, str]):  Example: fixed.
        unit (Union[Unset, str]):
        initial_amount (Union[Unset, str]):  Example: 2.0.
        member_id (Union[Unset, int]): The initiator of the pool action
        stock_id (Union[Unset, int]): The pooled stock ID
        stock_name (Union[Unset, str]): The pooled stock name
        stock_url (Union[Unset, str]):  Example: /storage/stocks/620.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    unit_type: Union[Unset, str] = UNSET
    pool_type: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    initial_amount: Union[Unset, str] = UNSET
    member_id: Union[Unset, int] = UNSET
    stock_id: Union[Unset, int] = UNSET
    stock_name: Union[Unset, str] = UNSET
    stock_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        unit_type = self.unit_type

        pool_type = self.pool_type

        unit = self.unit

        initial_amount = self.initial_amount

        member_id = self.member_id

        stock_id = self.stock_id

        stock_name = self.stock_name

        stock_url = self.stock_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type
        if pool_type is not UNSET:
            field_dict["pool_type"] = pool_type
        if unit is not UNSET:
            field_dict["unit"] = unit
        if initial_amount is not UNSET:
            field_dict["initial_amount"] = initial_amount
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if stock_id is not UNSET:
            field_dict["stock_id"] = stock_id
        if stock_name is not UNSET:
            field_dict["stock_name"] = stock_name
        if stock_url is not UNSET:
            field_dict["stock_url"] = stock_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        unit_type = d.pop("unit_type", UNSET)

        pool_type = d.pop("pool_type", UNSET)

        unit = d.pop("unit", UNSET)

        initial_amount = d.pop("initial_amount", UNSET)

        member_id = d.pop("member_id", UNSET)

        stock_id = d.pop("stock_id", UNSET)

        stock_name = d.pop("stock_name", UNSET)

        stock_url = d.pop("stock_url", UNSET)

        post_api_v1_pool_events_response_200 = cls(
            id=id,
            name=name,
            unit_type=unit_type,
            pool_type=pool_type,
            unit=unit,
            initial_amount=initial_amount,
            member_id=member_id,
            stock_id=stock_id,
            stock_name=stock_name,
            stock_url=stock_url,
        )

        post_api_v1_pool_events_response_200.additional_properties = d
        return post_api_v1_pool_events_response_200

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
