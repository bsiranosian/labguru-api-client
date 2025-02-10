from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RodentCageBaseRequestItem")


@_attrs_define
class RodentCageBaseRequestItem:
    """
    Attributes:
        name (str): The name of the Rodent cage Example: rodent cage 1.
        breeding (Union[Unset, int]): Breeding - 1(Yes)/2(No) - by default it's 1 Example: 1.
        parent_id (Union[Unset, int]): id of storage location Example: 1.
        description (Union[Unset, str]): Description of the gene Example: General description.
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
    """

    name: str
    breeding: Union[Unset, int] = UNSET
    parent_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        breeding = self.breeding

        parent_id = self.parent_id

        description = self.description

        owner_id = self.owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if breeding is not UNSET:
            field_dict["breeding"] = breeding
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if description is not UNSET:
            field_dict["description"] = description
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        breeding = d.pop("breeding", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        description = d.pop("description", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        rodent_cage_base_request_item = cls(
            name=name,
            breeding=breeding,
            parent_id=parent_id,
            description=description,
            owner_id=owner_id,
        )

        rodent_cage_base_request_item.additional_properties = d
        return rodent_cage_base_request_item

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
