import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlantBaseRequestItem")


@_attrs_define
class PlantBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The botanical name of the plant.
        owner_id (Union[Unset, int]): ID of the owner - if omitted, will default to your id Example: Your member id.
        phenotype (Union[Unset, str]): Observable physical or biochemical characteristics of the plant
        genotype (Union[Unset, str]): The genetic makeup of the plant
        generation (Union[Unset, str]): Generation of the plant
        harvest_date (Union[Unset, datetime.date]): The date when the plant was harvested, formatted as YYYY-MM-DD
            Example: 2021-03-11.
        source (Union[Unset, str]): The origin of the plant
        description (Union[Unset, str]): Description of the plant
    """

    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    phenotype: Union[Unset, str] = UNSET
    genotype: Union[Unset, str] = UNSET
    generation: Union[Unset, str] = UNSET
    harvest_date: Union[Unset, datetime.date] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_id = self.owner_id

        phenotype = self.phenotype

        genotype = self.genotype

        generation = self.generation

        harvest_date: Union[Unset, str] = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if generation is not UNSET:
            field_dict["generation"] = generation
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
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

        phenotype = d.pop("phenotype", UNSET)

        genotype = d.pop("genotype", UNSET)

        generation = d.pop("generation", UNSET)

        _harvest_date = d.pop("harvest_date", UNSET)
        harvest_date: Union[Unset, datetime.date]
        if isinstance(_harvest_date, Unset):
            harvest_date = UNSET
        else:
            harvest_date = isoparse(_harvest_date).date()

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        plant_base_request_item = cls(
            name=name,
            owner_id=owner_id,
            phenotype=phenotype,
            genotype=genotype,
            generation=generation,
            harvest_date=harvest_date,
            source=source,
            description=description,
        )

        plant_base_request_item.additional_properties = d
        return plant_base_request_item

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
