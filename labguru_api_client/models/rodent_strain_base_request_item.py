from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RodentStrainBaseRequestItem")


@_attrs_define
class RodentStrainBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the strain Example: rodi.
        alternative_name (Union[Unset, str]): additional name for the strain Example: ro.
        transgene (Union[Unset, str]): Transgene
        genotype (Union[Unset, str]): Genotype
        phenotype (Union[Unset, str]): Phenotype
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        source (Union[Unset, str]): Source
        description (Union[Unset, str]): Description of the strain Example: General description.
    """

    name: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    transgene: Union[Unset, str] = UNSET
    genotype: Union[Unset, str] = UNSET
    phenotype: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alternative_name = self.alternative_name

        transgene = self.transgene

        genotype = self.genotype

        phenotype = self.phenotype

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
        if transgene is not UNSET:
            field_dict["transgene"] = transgene
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
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

        transgene = d.pop("transgene", UNSET)

        genotype = d.pop("genotype", UNSET)

        phenotype = d.pop("phenotype", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        rodent_strain_base_request_item = cls(
            name=name,
            alternative_name=alternative_name,
            transgene=transgene,
            genotype=genotype,
            phenotype=phenotype,
            owner_id=owner_id,
            source=source,
            description=description,
        )

        rodent_strain_base_request_item.additional_properties = d
        return rodent_strain_base_request_item

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
