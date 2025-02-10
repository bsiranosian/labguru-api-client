from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlasmidBaseRequestItem")


@_attrs_define
class PlasmidBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): The name of the plasmid
        alternative_name (Union[Unset, str]): Any alternative name by which the plasmid may be known
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        length (Union[Unset, int]): The total number of base pairs (bp) in the plasmid’s DNA sequence.
        usage (Union[Unset, str]): Intended or common uses of the plasmid (cloning, gene expression, etc.)
        host (Union[Unset, str]): Typical host organism for the plasmid
        resistance (Union[Unset, str]): Antibiotic resistance markers present in the plasmid
        clone_number (Union[Unset, str]): Unique identifier or clone number associated with the plasmid
        source (Union[Unset, str]): Origin or provider of the plasmid
        sequence (Union[Unset, str]): The nucleotide sequence of the plasmid
        description (Union[Unset, str]): A detailed description of the plasmid
    """

    title: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    length: Union[Unset, int] = UNSET
    usage: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    resistance: Union[Unset, str] = UNSET
    clone_number: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    sequence: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        alternative_name = self.alternative_name

        owner_id = self.owner_id

        length = self.length

        usage = self.usage

        host = self.host

        resistance = self.resistance

        clone_number = self.clone_number

        source = self.source

        sequence = self.sequence

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if length is not UNSET:
            field_dict["length"] = length
        if usage is not UNSET:
            field_dict["usage"] = usage
        if host is not UNSET:
            field_dict["host"] = host
        if resistance is not UNSET:
            field_dict["resistance"] = resistance
        if clone_number is not UNSET:
            field_dict["clone_number"] = clone_number
        if source is not UNSET:
            field_dict["source"] = source
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        length = d.pop("length", UNSET)

        usage = d.pop("usage", UNSET)

        host = d.pop("host", UNSET)

        resistance = d.pop("resistance", UNSET)

        clone_number = d.pop("clone_number", UNSET)

        source = d.pop("source", UNSET)

        sequence = d.pop("sequence", UNSET)

        description = d.pop("description", UNSET)

        plasmid_base_request_item = cls(
            title=title,
            alternative_name=alternative_name,
            owner_id=owner_id,
            length=length,
            usage=usage,
            host=host,
            resistance=resistance,
            clone_number=clone_number,
            source=source,
            sequence=sequence,
            description=description,
        )

        plasmid_base_request_item.additional_properties = d
        return plasmid_base_request_item

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
