from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cell_line_base_request_item import CellLineBaseRequestItem


T = TypeVar("T", bound="CellLineBaseRequest")


@_attrs_define
class CellLineBaseRequest:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        item (Union[Unset, CellLineBaseRequestItem]):
    """

    token: str
    item: Union[Unset, "CellLineBaseRequestItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cell_line_base_request_item import CellLineBaseRequestItem

        d = src_dict.copy()
        token = d.pop("token")

        _item = d.pop("item", UNSET)
        item: Union[Unset, CellLineBaseRequestItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = CellLineBaseRequestItem.from_dict(_item)

        cell_line_base_request = cls(
            token=token,
            item=item,
        )

        cell_line_base_request.additional_properties = d
        return cell_line_base_request

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
