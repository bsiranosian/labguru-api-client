from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TissueBaseRequestItem")


@_attrs_define
class TissueBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the tissue
        alternative_name (Union[Unset, str]): An alternative name for the tissue
        species (Union[Unset, str]): The species from which the tissue is derived
        genotype_phenotype (Union[Unset, str]): Genotype/phenotype
        animal_details (Union[Unset, str]): Detailed information about the animal from which the tissue was harvested
        tissue_type (Union[Unset, str]): The type of the tissue
        harvest_date (Union[Unset, str]): Harvest date - in the following format (yyyy-mm-dd) Example: 2021-06-21.
        fixation_embedding_procedure (Union[Unset, str]): Fixation/embedding procedure
        applications (Union[Unset, str]): Applications
        storage_conditions (Union[Unset, str]): Storage conditions
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        source (Union[Unset, str]): The origin of the tissue
        description (Union[Unset, str]): Description of the tissue
    """

    name: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    species: Union[Unset, str] = UNSET
    genotype_phenotype: Union[Unset, str] = UNSET
    animal_details: Union[Unset, str] = UNSET
    tissue_type: Union[Unset, str] = UNSET
    harvest_date: Union[Unset, str] = UNSET
    fixation_embedding_procedure: Union[Unset, str] = UNSET
    applications: Union[Unset, str] = UNSET
    storage_conditions: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alternative_name = self.alternative_name

        species = self.species

        genotype_phenotype = self.genotype_phenotype

        animal_details = self.animal_details

        tissue_type = self.tissue_type

        harvest_date = self.harvest_date

        fixation_embedding_procedure = self.fixation_embedding_procedure

        applications = self.applications

        storage_conditions = self.storage_conditions

        owner_id = self.owner_id

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if species is not UNSET:
            field_dict["species"] = species
        if genotype_phenotype is not UNSET:
            field_dict["genotype_phenotype"] = genotype_phenotype
        if animal_details is not UNSET:
            field_dict["animal_details"] = animal_details
        if tissue_type is not UNSET:
            field_dict["tissue_type"] = tissue_type
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if fixation_embedding_procedure is not UNSET:
            field_dict["fixation_embedding_procedure"] = fixation_embedding_procedure
        if applications is not UNSET:
            field_dict["applications"] = applications
        if storage_conditions is not UNSET:
            field_dict["storage_conditions"] = storage_conditions
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        species = d.pop("species", UNSET)

        genotype_phenotype = d.pop("genotype_phenotype", UNSET)

        animal_details = d.pop("animal_details", UNSET)

        tissue_type = d.pop("tissue_type", UNSET)

        harvest_date = d.pop("harvest_date", UNSET)

        fixation_embedding_procedure = d.pop("fixation_embedding_procedure", UNSET)

        applications = d.pop("applications", UNSET)

        storage_conditions = d.pop("storage_conditions", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        tissue_base_request_item = cls(
            name=name,
            alternative_name=alternative_name,
            species=species,
            genotype_phenotype=genotype_phenotype,
            animal_details=animal_details,
            tissue_type=tissue_type,
            harvest_date=harvest_date,
            fixation_embedding_procedure=fixation_embedding_procedure,
            applications=applications,
            storage_conditions=storage_conditions,
            owner_id=owner_id,
            source=source,
            description=description,
        )

        tissue_base_request_item.additional_properties = d
        return tissue_base_request_item

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
