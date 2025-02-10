from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProteinBaseRequestItem")


@_attrs_define
class ProteinBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the protein
        owner_id (Union[Unset, int]): ID of the owner - if omitted, will default to your id Example: Your member id.
        alternative_name (Union[Unset, str]): An additional name for the protein
        gene (Union[Unset, str]):  The gene from which the protein is derived
        species (Union[Unset, str]): The species from which the protein originates
        lg_mutations (Union[Unset, str]): List of mutations in the protein structure
        chemical_modifications (Union[Unset, str]): Details any chemical modifications the protein has undergone
        tag (Union[Unset, str]): A label or tag attached to the protein
        purification_method (Union[Unset, str]): The method used to purify the protein from other biological components
        mw (Union[Unset, str]): The molecular weight of the protein
        extinction_coefficient_280nm (Union[Unset, str]): The extinction coefficient at 280 nm
        storage_buffer (Union[Unset, str]): The buffer solution in which the protein is stored
        storage_temperature (Union[Unset, str]): The temperature in which the protein is stored
        source (Union[Unset, str]): The protein source
        sequence (Union[Unset, str]): The amino acid sequence of the protein
        description (Union[Unset, str]): A detailed description of the protein
    """

    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    gene: Union[Unset, str] = UNSET
    species: Union[Unset, str] = UNSET
    lg_mutations: Union[Unset, str] = UNSET
    chemical_modifications: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    purification_method: Union[Unset, str] = UNSET
    mw: Union[Unset, str] = UNSET
    extinction_coefficient_280nm: Union[Unset, str] = UNSET
    storage_buffer: Union[Unset, str] = UNSET
    storage_temperature: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    sequence: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_id = self.owner_id

        alternative_name = self.alternative_name

        gene = self.gene

        species = self.species

        lg_mutations = self.lg_mutations

        chemical_modifications = self.chemical_modifications

        tag = self.tag

        purification_method = self.purification_method

        mw = self.mw

        extinction_coefficient_280nm = self.extinction_coefficient_280nm

        storage_buffer = self.storage_buffer

        storage_temperature = self.storage_temperature

        source = self.source

        sequence = self.sequence

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if gene is not UNSET:
            field_dict["gene"] = gene
        if species is not UNSET:
            field_dict["species"] = species
        if lg_mutations is not UNSET:
            field_dict["lg_mutations"] = lg_mutations
        if chemical_modifications is not UNSET:
            field_dict["chemical_modifications"] = chemical_modifications
        if tag is not UNSET:
            field_dict["tag"] = tag
        if purification_method is not UNSET:
            field_dict["purification_method"] = purification_method
        if mw is not UNSET:
            field_dict["mw"] = mw
        if extinction_coefficient_280nm is not UNSET:
            field_dict["extinction_coefficient_280nm"] = extinction_coefficient_280nm
        if storage_buffer is not UNSET:
            field_dict["storage_buffer"] = storage_buffer
        if storage_temperature is not UNSET:
            field_dict["storage_temperature"] = storage_temperature
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
        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        gene = d.pop("gene", UNSET)

        species = d.pop("species", UNSET)

        lg_mutations = d.pop("lg_mutations", UNSET)

        chemical_modifications = d.pop("chemical_modifications", UNSET)

        tag = d.pop("tag", UNSET)

        purification_method = d.pop("purification_method", UNSET)

        mw = d.pop("mw", UNSET)

        extinction_coefficient_280nm = d.pop("extinction_coefficient_280nm", UNSET)

        storage_buffer = d.pop("storage_buffer", UNSET)

        storage_temperature = d.pop("storage_temperature", UNSET)

        source = d.pop("source", UNSET)

        sequence = d.pop("sequence", UNSET)

        description = d.pop("description", UNSET)

        protein_base_request_item = cls(
            name=name,
            owner_id=owner_id,
            alternative_name=alternative_name,
            gene=gene,
            species=species,
            lg_mutations=lg_mutations,
            chemical_modifications=chemical_modifications,
            tag=tag,
            purification_method=purification_method,
            mw=mw,
            extinction_coefficient_280nm=extinction_coefficient_280nm,
            storage_buffer=storage_buffer,
            storage_temperature=storage_temperature,
            source=source,
            sequence=sequence,
            description=description,
        )

        protein_base_request_item.additional_properties = d
        return protein_base_request_item

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
