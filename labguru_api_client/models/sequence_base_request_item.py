from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SequenceBaseRequestItem")


@_attrs_define
class SequenceBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): The name of the sequence
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        seq (Union[Unset, str]): The actual sequence data in characters
        kind (Union[Unset, int]): sequence type: DNA = 1, CDNA = 2, RNA = 3, PROBE = 4, PROTEIN = 5 Example: 2.
        accsesion (Union[Unset, str]): The unique accession number assigned to the sequence
        organism (Union[Unset, str]): The organism from which the sequence is derived
        description (Union[Unset, str]): Description of the sequence
    """

    title: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    seq: Union[Unset, str] = UNSET
    kind: Union[Unset, int] = UNSET
    accsesion: Union[Unset, str] = UNSET
    organism: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        owner_id = self.owner_id

        seq = self.seq

        kind = self.kind

        accsesion = self.accsesion

        organism = self.organism

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if seq is not UNSET:
            field_dict["seq"] = seq
        if kind is not UNSET:
            field_dict["kind"] = kind
        if accsesion is not UNSET:
            field_dict["accsesion"] = accsesion
        if organism is not UNSET:
            field_dict["organism"] = organism
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        seq = d.pop("seq", UNSET)

        kind = d.pop("kind", UNSET)

        accsesion = d.pop("accsesion", UNSET)

        organism = d.pop("organism", UNSET)

        description = d.pop("description", UNSET)

        sequence_base_request_item = cls(
            title=title,
            owner_id=owner_id,
            seq=seq,
            kind=kind,
            accsesion=accsesion,
            organism=organism,
            description=description,
        )

        sequence_base_request_item.additional_properties = d
        return sequence_base_request_item

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
