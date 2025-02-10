import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AntibodyBaseRequestItem")


@_attrs_define
class AntibodyBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): The name of the antibody
        owner_id (Union[Unset, int]): The ID of the owner - by default it's your member id Example: Your member id.
        alternative_name (Union[Unset, str]): An additional name for the antibody
        antigene (Union[Unset, str]): Antigen / immunogen
        tags_fluorophores (Union[Unset, str]): Tags / fluorophores
        clone_field (Union[Unset, str]): The clone from which the antibody was derived.
        isotype (Union[Unset, str]): The class or type of the antibody (e.g., IgG, IgM).
        preparation_date (Union[Unset, datetime.date]): The date on which the antibody was prepared, formatted as YYYY-
            MM-DD. Example: yyyy-mm-dd.
        source (Union[Unset, str]): The origin or source from which the antibody was obtained.
        immune (Union[Unset, int]): Indicates the antibody's clonality: "Monoclonal" (immune = 1), "Polyclonal" (immune
            = 0), or "None" (Empty value). Example: 1.
        organism_id (Union[Unset, int]): The ID for the organism in which the antibody was raised. This ID corresponds
            to specific organisms (e.g., 5 for Mouse, 6 for Chicken, etc.).
        reacts_with (Union[Unset, str]): Specifies the organism or group the antibody is reactive with, chosen from a
            predefined list of options such as "Mouse", "Human", "Chicken", and "Zebrafish", etc. Example: Mouse.
        description (Union[Unset, str]): A detailed description of the antibody
    """

    title: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    antigene: Union[Unset, str] = UNSET
    tags_fluorophores: Union[Unset, str] = UNSET
    clone_field: Union[Unset, str] = UNSET
    isotype: Union[Unset, str] = UNSET
    preparation_date: Union[Unset, datetime.date] = UNSET
    source: Union[Unset, str] = UNSET
    immune: Union[Unset, int] = UNSET
    organism_id: Union[Unset, int] = UNSET
    reacts_with: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        owner_id = self.owner_id

        alternative_name = self.alternative_name

        antigene = self.antigene

        tags_fluorophores = self.tags_fluorophores

        clone_field = self.clone_field

        isotype = self.isotype

        preparation_date: Union[Unset, str] = UNSET
        if not isinstance(self.preparation_date, Unset):
            preparation_date = self.preparation_date.isoformat()

        source = self.source

        immune = self.immune

        organism_id = self.organism_id

        reacts_with = self.reacts_with

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if antigene is not UNSET:
            field_dict["antigene"] = antigene
        if tags_fluorophores is not UNSET:
            field_dict["tags_fluorophores"] = tags_fluorophores
        if clone_field is not UNSET:
            field_dict["clone_field"] = clone_field
        if isotype is not UNSET:
            field_dict["isotype"] = isotype
        if preparation_date is not UNSET:
            field_dict["preparation_date"] = preparation_date
        if source is not UNSET:
            field_dict["source"] = source
        if immune is not UNSET:
            field_dict["immune"] = immune
        if organism_id is not UNSET:
            field_dict["organism_id"] = organism_id
        if reacts_with is not UNSET:
            field_dict["reacts_with"] = reacts_with
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        antigene = d.pop("antigene", UNSET)

        tags_fluorophores = d.pop("tags_fluorophores", UNSET)

        clone_field = d.pop("clone_field", UNSET)

        isotype = d.pop("isotype", UNSET)

        _preparation_date = d.pop("preparation_date", UNSET)
        preparation_date: Union[Unset, datetime.date]
        if isinstance(_preparation_date, Unset):
            preparation_date = UNSET
        else:
            preparation_date = isoparse(_preparation_date).date()

        source = d.pop("source", UNSET)

        immune = d.pop("immune", UNSET)

        organism_id = d.pop("organism_id", UNSET)

        reacts_with = d.pop("reacts_with", UNSET)

        description = d.pop("description", UNSET)

        antibody_base_request_item = cls(
            title=title,
            owner_id=owner_id,
            alternative_name=alternative_name,
            antigene=antigene,
            tags_fluorophores=tags_fluorophores,
            clone_field=clone_field,
            isotype=isotype,
            preparation_date=preparation_date,
            source=source,
            immune=immune,
            organism_id=organism_id,
            reacts_with=reacts_with,
            description=description,
        )

        antibody_base_request_item.additional_properties = d
        return antibody_base_request_item

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
