import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSectionItem")


@_attrs_define
class UpdateSectionItem:
    r"""
    Attributes:
        name (Union[Unset, str]): the name of the section Example: Section-1.
        container_id (Union[Unset, int]): the id of the experiment/protocol/report the section belongs to Example: 2.
        container_type (Union[Unset, str]): the type of the container -
            Projects::Experiment\Knowledgebase::Protocol\Knowledgebase::Report Example: Projects::Experiment.
        position (Union[Unset, datetime.date]): the section position Example: 1.
    """

    name: Union[Unset, str] = UNSET
    container_id: Union[Unset, int] = UNSET
    container_type: Union[Unset, str] = UNSET
    position: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        container_id = self.container_id

        container_type = self.container_type

        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if container_id is not UNSET:
            field_dict["container_id"] = container_id
        if container_type is not UNSET:
            field_dict["container_type"] = container_type
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        container_id = d.pop("container_id", UNSET)

        container_type = d.pop("container_type", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, datetime.date]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = isoparse(_position).date()

        update_section_item = cls(
            name=name,
            container_id=container_id,
            container_type=container_type,
            position=position,
        )

        update_section_item.additional_properties = d
        return update_section_item

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
