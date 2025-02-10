from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeedBaseRequestItem")


@_attrs_define
class SeedBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the seed
        owner_id (Union[Unset, int]): id of the owner - if omitted, will default to your member id Example: Your member
            id.
        genotype (Union[Unset, str]): Genetic makeup of the seed
        phenotype (Union[Unset, str]): Observable physical or biochemical characteristics of the seed
        generation (Union[Unset, str]): Generational stage of the seed Example: F0.
        male_parent_id (Union[Unset, int]): The ID of the male parent plant from your Labguru plants collection, if
            applicable.
        female_parent_id (Union[Unset, int]): The ID of the female parent plant from your Labguru plants collection, if
            applicable.
        source (Union[Unset, str]): Origin of the seed
        description (Union[Unset, str]): Description of the seed
    """

    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    genotype: Union[Unset, str] = UNSET
    phenotype: Union[Unset, str] = UNSET
    generation: Union[Unset, str] = UNSET
    male_parent_id: Union[Unset, int] = UNSET
    female_parent_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_id = self.owner_id

        genotype = self.genotype

        phenotype = self.phenotype

        generation = self.generation

        male_parent_id = self.male_parent_id

        female_parent_id = self.female_parent_id

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
        if generation is not UNSET:
            field_dict["generation"] = generation
        if male_parent_id is not UNSET:
            field_dict["male_parent_id"] = male_parent_id
        if female_parent_id is not UNSET:
            field_dict["female_parent_id"] = female_parent_id
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

        genotype = d.pop("genotype", UNSET)

        phenotype = d.pop("phenotype", UNSET)

        generation = d.pop("generation", UNSET)

        male_parent_id = d.pop("male_parent_id", UNSET)

        female_parent_id = d.pop("female_parent_id", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        seed_base_request_item = cls(
            name=name,
            owner_id=owner_id,
            genotype=genotype,
            phenotype=phenotype,
            generation=generation,
            male_parent_id=male_parent_id,
            female_parent_id=female_parent_id,
            source=source,
            description=description,
        )

        seed_base_request_item.additional_properties = d
        return seed_base_request_item

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
