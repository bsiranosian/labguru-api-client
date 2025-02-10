from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSectionItem")


@_attrs_define
class CreateSectionItem:
    r"""
    Attributes:
        name (str): the name of the section Example: Section-1.
        container_id (int): the id of the experiment/protocol/report the section belongs to Example: 2.
        container_type (str): the type of the container -
            Projects::Experiment\Knowledgebase::Protocol\Knowledgebase::Report Example: Projects::Experiment.
        position (Union[Unset, int]): the section position Example: 1.
    """

    name: str
    container_id: int
    container_type: str
    position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        container_id = self.container_id

        container_type = self.container_type

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "container_id": container_id,
                "container_type": container_type,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        container_id = d.pop("container_id")

        container_type = d.pop("container_type")

        position = d.pop("position", UNSET)

        create_section_item = cls(
            name=name,
            container_id=container_id,
            container_type=container_type,
            position=position,
        )

        create_section_item.additional_properties = d
        return create_section_item

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
