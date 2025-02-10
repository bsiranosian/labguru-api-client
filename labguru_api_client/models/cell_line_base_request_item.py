from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CellLineBaseRequestItem")


@_attrs_define
class CellLineBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the cell line
        owner_id (Union[Unset, int]): The ID of the owner - by default it's your member id Example: Your member id.
        organism (Union[Unset, str]): The organism from which the cells were originated
        tissue (Union[Unset, str]): The tissue from which the cells were extracted
        medium_and_serum (Union[Unset, str]): A supplement used for cultivating cells
        source (Union[Unset, str]): The location or environment from which the cells were originated
        description (Union[Unset, str]): A detailed description of the cell line
    """

    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    organism: Union[Unset, str] = UNSET
    tissue: Union[Unset, str] = UNSET
    medium_and_serum: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_id = self.owner_id

        organism = self.organism

        tissue = self.tissue

        medium_and_serum = self.medium_and_serum

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if organism is not UNSET:
            field_dict["organism"] = organism
        if tissue is not UNSET:
            field_dict["tissue"] = tissue
        if medium_and_serum is not UNSET:
            field_dict["medium_and_serum"] = medium_and_serum
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        organism = d.pop("organism", UNSET)

        tissue = d.pop("tissue", UNSET)

        medium_and_serum = d.pop("medium_and_serum", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        cell_line_base_request_item = cls(
            name=name,
            owner_id=owner_id,
            organism=organism,
            tissue=tissue,
            medium_and_serum=medium_and_serum,
            source=source,
            description=description,
        )

        cell_line_base_request_item.additional_properties = d
        return cell_line_base_request_item

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
