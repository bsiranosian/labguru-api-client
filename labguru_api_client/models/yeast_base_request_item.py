from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YeastBaseRequestItem")


@_attrs_define
class YeastBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the yeast
        description (Union[Unset, str]): Description of the yeast
        reproduction (Union[Unset, str]): Details of the mode of reproduction for the yeast
        genetic_background (Union[Unset, str]): yeast's genetic lineage or background
        transgenic_features (Union[Unset, str]): Transgenic Features
        phenotype (Union[Unset, str]): Observable characteristics of the yeast
        source (Union[Unset, str]): Origin of the yeast strain
        owner_id (Union[Unset, int]): id of the owner - if omitted, will default to your member id Example: Your member
            id.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    reproduction: Union[Unset, str] = UNSET
    genetic_background: Union[Unset, str] = UNSET
    transgenic_features: Union[Unset, str] = UNSET
    phenotype: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        reproduction = self.reproduction

        genetic_background = self.genetic_background

        transgenic_features = self.transgenic_features

        phenotype = self.phenotype

        source = self.source

        owner_id = self.owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if reproduction is not UNSET:
            field_dict["reproduction"] = reproduction
        if genetic_background is not UNSET:
            field_dict["genetic_background"] = genetic_background
        if transgenic_features is not UNSET:
            field_dict["transgenic_features"] = transgenic_features
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
        if source is not UNSET:
            field_dict["source"] = source
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        reproduction = d.pop("reproduction", UNSET)

        genetic_background = d.pop("genetic_background", UNSET)

        transgenic_features = d.pop("transgenic_features", UNSET)

        phenotype = d.pop("phenotype", UNSET)

        source = d.pop("source", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        yeast_base_request_item = cls(
            name=name,
            description=description,
            reproduction=reproduction,
            genetic_background=genetic_background,
            transgenic_features=transgenic_features,
            phenotype=phenotype,
            source=source,
            owner_id=owner_id,
        )

        yeast_base_request_item.additional_properties = d
        return yeast_base_request_item

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
