from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyBaseRequestItem")


@_attrs_define
class FlyBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the fly
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        source (Union[Unset, str]): Origin of the fly.
        genotype (Union[Unset, str]): Genetic makeup.
        phenotype (Union[Unset, str]): Observable characteristics.
        breakpoints_insertions (Union[Unset, str]): Genetic insertion points.
        ch_number (Union[Unset, str]): Chromosome number.
        ch_te (Union[Unset, str]): Transposable element in chromosome.
        description (Union[Unset, str]): Description of the fly
    """

    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    genotype: Union[Unset, str] = UNSET
    phenotype: Union[Unset, str] = UNSET
    breakpoints_insertions: Union[Unset, str] = UNSET
    ch_number: Union[Unset, str] = UNSET
    ch_te: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_id = self.owner_id

        source = self.source

        genotype = self.genotype

        phenotype = self.phenotype

        breakpoints_insertions = self.breakpoints_insertions

        ch_number = self.ch_number

        ch_te = self.ch_te

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if source is not UNSET:
            field_dict["source"] = source
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
        if breakpoints_insertions is not UNSET:
            field_dict["breakpoints_insertions"] = breakpoints_insertions
        if ch_number is not UNSET:
            field_dict["ch_number"] = ch_number
        if ch_te is not UNSET:
            field_dict["ch_te"] = ch_te
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        source = d.pop("source", UNSET)

        genotype = d.pop("genotype", UNSET)

        phenotype = d.pop("phenotype", UNSET)

        breakpoints_insertions = d.pop("breakpoints_insertions", UNSET)

        ch_number = d.pop("ch_number", UNSET)

        ch_te = d.pop("ch_te", UNSET)

        description = d.pop("description", UNSET)

        fly_base_request_item = cls(
            name=name,
            owner_id=owner_id,
            source=source,
            genotype=genotype,
            phenotype=phenotype,
            breakpoints_insertions=breakpoints_insertions,
            ch_number=ch_number,
            ch_te=ch_te,
            description=description,
        )

        fly_base_request_item.additional_properties = d
        return fly_base_request_item

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
