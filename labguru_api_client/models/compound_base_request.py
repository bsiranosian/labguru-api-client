from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compound_base_request_item import CompoundBaseRequestItem


T = TypeVar("T", bound="CompoundBaseRequest")


@_attrs_define
class CompoundBaseRequest:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        smiles (Union[Unset, str]):  Example: C(=O)N1CCC(CCCC(=O)c2ccc(Cl)n(Cc3ncc(o3)-c3ccc(Cl)cc3)c2=O)CC1.
        item (Union[Unset, CompoundBaseRequestItem]):
    """

    token: str
    smiles: Union[Unset, str] = UNSET
    item: Union[Unset, "CompoundBaseRequestItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        smiles = self.smiles

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
        if smiles is not UNSET:
            field_dict["smiles"] = smiles
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.compound_base_request_item import CompoundBaseRequestItem

        d = src_dict.copy()
        token = d.pop("token")

        smiles = d.pop("smiles", UNSET)

        _item = d.pop("item", UNSET)
        item: Union[Unset, CompoundBaseRequestItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = CompoundBaseRequestItem.from_dict(_item)

        compound_base_request = cls(
            token=token,
            smiles=smiles,
            item=item,
        )

        compound_base_request.additional_properties = d
        return compound_base_request

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
