from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BacteriumBaseRequestItem")


@_attrs_define
class BacteriumBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the bacterium
        sensitivity (Union[Unset, str]): Details the bacterium’s sensitivity to antibiotics or other agents.
        strain (Union[Unset, str]): The specific strain of the bacterium
        source (Union[Unset, str]): The origin or isolation source of the bacterium (e.g., environmental, clinical).
        owner_id (Union[Unset, int]): The ID of the owner - by default it's your member id Example: Your member id.
        description (Union[Unset, str]): A detailed description of the bacterium
    """

    name: Union[Unset, str] = UNSET
    sensitivity: Union[Unset, str] = UNSET
    strain: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sensitivity = self.sensitivity

        strain = self.strain

        source = self.source

        owner_id = self.owner_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity
        if strain is not UNSET:
            field_dict["strain"] = strain
        if source is not UNSET:
            field_dict["source"] = source
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        sensitivity = d.pop("sensitivity", UNSET)

        strain = d.pop("strain", UNSET)

        source = d.pop("source", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        description = d.pop("description", UNSET)

        bacterium_base_request_item = cls(
            name=name,
            sensitivity=sensitivity,
            strain=strain,
            source=source,
            owner_id=owner_id,
            description=description,
        )

        bacterium_base_request_item.additional_properties = d
        return bacterium_base_request_item

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
