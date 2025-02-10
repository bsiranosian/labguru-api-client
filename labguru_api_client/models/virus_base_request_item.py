from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirusBaseRequestItem")


@_attrs_define
class VirusBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the virus
        alternative_name (Union[Unset, str]): alternative name for the virus
        gene_insert (Union[Unset, str]): Specific gene or genetic insert present in the virus
        virus_type (Union[Unset, str]): The virus type
        plasmid (Union[Unset, str]): The plasmid that is used in the creation or manipulation of the virus
        serotype_strain (Union[Unset, str]): serotype or strain of the virus
        mutations_deletions (Union[Unset, str]): genetic mutations or deletions within the virus details
        tag (Union[Unset, str]): Tag
        selectable_marker (Union[Unset, str]): Selectable marker
        producer_cell_type (Union[Unset, str]): Producer cell type
        viral_coat (Union[Unset, str]): Viral coat
        tropism (Union[Unset, str]): Tropism
        species (Union[Unset, str]): The species from which the virus was isolated or generated
        safety_information (Union[Unset, str]): safety information details
        storage_conditions (Union[Unset, str]): Conditions under which the virus should be stored
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        source (Union[Unset, str]): The origin of the virus
        description (Union[Unset, str]): Description of the virus
    """

    name: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    gene_insert: Union[Unset, str] = UNSET
    virus_type: Union[Unset, str] = UNSET
    plasmid: Union[Unset, str] = UNSET
    serotype_strain: Union[Unset, str] = UNSET
    mutations_deletions: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    selectable_marker: Union[Unset, str] = UNSET
    producer_cell_type: Union[Unset, str] = UNSET
    viral_coat: Union[Unset, str] = UNSET
    tropism: Union[Unset, str] = UNSET
    species: Union[Unset, str] = UNSET
    safety_information: Union[Unset, str] = UNSET
    storage_conditions: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alternative_name = self.alternative_name

        gene_insert = self.gene_insert

        virus_type = self.virus_type

        plasmid = self.plasmid

        serotype_strain = self.serotype_strain

        mutations_deletions = self.mutations_deletions

        tag = self.tag

        selectable_marker = self.selectable_marker

        producer_cell_type = self.producer_cell_type

        viral_coat = self.viral_coat

        tropism = self.tropism

        species = self.species

        safety_information = self.safety_information

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
        if gene_insert is not UNSET:
            field_dict["gene_insert"] = gene_insert
        if virus_type is not UNSET:
            field_dict["virus_type"] = virus_type
        if plasmid is not UNSET:
            field_dict["plasmid"] = plasmid
        if serotype_strain is not UNSET:
            field_dict["serotype_strain"] = serotype_strain
        if mutations_deletions is not UNSET:
            field_dict["mutations_deletions"] = mutations_deletions
        if tag is not UNSET:
            field_dict["tag"] = tag
        if selectable_marker is not UNSET:
            field_dict["selectable_marker"] = selectable_marker
        if producer_cell_type is not UNSET:
            field_dict["producer_cell_type"] = producer_cell_type
        if viral_coat is not UNSET:
            field_dict["viral_coat"] = viral_coat
        if tropism is not UNSET:
            field_dict["tropism"] = tropism
        if species is not UNSET:
            field_dict["species"] = species
        if safety_information is not UNSET:
            field_dict["safety_information"] = safety_information
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

        gene_insert = d.pop("gene_insert", UNSET)

        virus_type = d.pop("virus_type", UNSET)

        plasmid = d.pop("plasmid", UNSET)

        serotype_strain = d.pop("serotype_strain", UNSET)

        mutations_deletions = d.pop("mutations_deletions", UNSET)

        tag = d.pop("tag", UNSET)

        selectable_marker = d.pop("selectable_marker", UNSET)

        producer_cell_type = d.pop("producer_cell_type", UNSET)

        viral_coat = d.pop("viral_coat", UNSET)

        tropism = d.pop("tropism", UNSET)

        species = d.pop("species", UNSET)

        safety_information = d.pop("safety_information", UNSET)

        storage_conditions = d.pop("storage_conditions", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        virus_base_request_item = cls(
            name=name,
            alternative_name=alternative_name,
            gene_insert=gene_insert,
            virus_type=virus_type,
            plasmid=plasmid,
            serotype_strain=serotype_strain,
            mutations_deletions=mutations_deletions,
            tag=tag,
            selectable_marker=selectable_marker,
            producer_cell_type=producer_cell_type,
            viral_coat=viral_coat,
            tropism=tropism,
            species=species,
            safety_information=safety_information,
            storage_conditions=storage_conditions,
            owner_id=owner_id,
            source=source,
            description=description,
        )

        virus_base_request_item.additional_properties = d
        return virus_base_request_item

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
