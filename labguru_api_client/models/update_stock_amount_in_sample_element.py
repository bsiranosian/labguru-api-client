from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStockAmountInSampleElement")


@_attrs_define
class UpdateStockAmountInSampleElement:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        unit_type (Union[Unset, str]): weight/volume Example: weight.
        element_id (Union[Unset, int]): the samples element id Example: 37.
        amount_used (Union[Unset, str]): amount_used Example: 15.
        unit_type_name (Union[Unset, str]): unit_type_name Example: mg.
        subtract (Union[Unset, str]): true Example: true.
        sample_id (Union[Unset, int]): the sample id Example: 6.
    """

    token: str
    unit_type: Union[Unset, str] = UNSET
    element_id: Union[Unset, int] = UNSET
    amount_used: Union[Unset, str] = UNSET
    unit_type_name: Union[Unset, str] = UNSET
    subtract: Union[Unset, str] = UNSET
    sample_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        unit_type = self.unit_type

        element_id = self.element_id

        amount_used = self.amount_used

        unit_type_name = self.unit_type_name

        subtract = self.subtract

        sample_id = self.sample_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type
        if element_id is not UNSET:
            field_dict["element_id"] = element_id
        if amount_used is not UNSET:
            field_dict["amount_used"] = amount_used
        if unit_type_name is not UNSET:
            field_dict["unit_type_name"] = unit_type_name
        if subtract is not UNSET:
            field_dict["subtract"] = subtract
        if sample_id is not UNSET:
            field_dict["sample_id"] = sample_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        unit_type = d.pop("unit_type", UNSET)

        element_id = d.pop("element_id", UNSET)

        amount_used = d.pop("amount_used", UNSET)

        unit_type_name = d.pop("unit_type_name", UNSET)

        subtract = d.pop("subtract", UNSET)

        sample_id = d.pop("sample_id", UNSET)

        update_stock_amount_in_sample_element = cls(
            token=token,
            unit_type=unit_type,
            element_id=element_id,
            amount_used=amount_used,
            unit_type_name=unit_type_name,
            subtract=subtract,
            sample_id=sample_id,
        )

        update_stock_amount_in_sample_element.additional_properties = d
        return update_stock_amount_in_sample_element

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
