from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FungusBaseRequestItem")


@_attrs_define
class FungusBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the fungus
        species (Union[Unset, str]): Biological species.
        phenotype (Union[Unset, str]): Observable traits.
        genotype (Union[Unset, str]): Genetic composition.
        host (Union[Unset, str]): Associated host organism.
        virulent (Union[Unset, str]): Virulence factor.
        sporulate (Union[Unset, str]): Ability to form spores.
        mycelia (Union[Unset, str]): Mycelial growth.
        fruiting_bodies (Union[Unset, str]): Presence of sporocarps.
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        source (Union[Unset, str]): The origin or source from which the fungus was obtained.
        description (Union[Unset, str]): Description of the fungus
    """

    name: Union[Unset, str] = UNSET
    species: Union[Unset, str] = UNSET
    phenotype: Union[Unset, str] = UNSET
    genotype: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    virulent: Union[Unset, str] = UNSET
    sporulate: Union[Unset, str] = UNSET
    mycelia: Union[Unset, str] = UNSET
    fruiting_bodies: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        species = self.species

        phenotype = self.phenotype

        genotype = self.genotype

        host = self.host

        virulent = self.virulent

        sporulate = self.sporulate

        mycelia = self.mycelia

        fruiting_bodies = self.fruiting_bodies

        owner_id = self.owner_id

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if species is not UNSET:
            field_dict["species"] = species
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if host is not UNSET:
            field_dict["host"] = host
        if virulent is not UNSET:
            field_dict["virulent"] = virulent
        if sporulate is not UNSET:
            field_dict["sporulate"] = sporulate
        if mycelia is not UNSET:
            field_dict["mycelia"] = mycelia
        if fruiting_bodies is not UNSET:
            field_dict["fruiting_bodies"] = fruiting_bodies
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

        species = d.pop("species", UNSET)

        phenotype = d.pop("phenotype", UNSET)

        genotype = d.pop("genotype", UNSET)

        host = d.pop("host", UNSET)

        virulent = d.pop("virulent", UNSET)

        sporulate = d.pop("sporulate", UNSET)

        mycelia = d.pop("mycelia", UNSET)

        fruiting_bodies = d.pop("fruiting_bodies", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        fungus_base_request_item = cls(
            name=name,
            species=species,
            phenotype=phenotype,
            genotype=genotype,
            host=host,
            virulent=virulent,
            sporulate=sporulate,
            mycelia=mycelia,
            fruiting_bodies=fruiting_bodies,
            owner_id=owner_id,
            source=source,
            description=description,
        )

        fungus_base_request_item.additional_properties = d
        return fungus_base_request_item

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
