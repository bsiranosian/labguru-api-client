from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1StocksIdUnmarkOutputBody")


@_attrs_define
class PostApiV1StocksIdUnmarkOutputBody:
    """
    Attributes:
        exp_id (Union[Unset, int]): the experiment id Example: 103.
    """

    exp_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exp_id = self.exp_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exp_id is not UNSET:
            field_dict["exp_id"] = exp_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        exp_id = d.pop("exp_id", UNSET)

        post_api_v1_stocks_id_unmark_output_body = cls(
            exp_id=exp_id,
        )

        post_api_v1_stocks_id_unmark_output_body.additional_properties = d
        return post_api_v1_stocks_id_unmark_output_body

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
