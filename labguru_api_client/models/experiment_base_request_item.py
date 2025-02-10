from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentBaseRequestItem")


@_attrs_define
class ExperimentBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): experiment title Example: My experiment.
        project_id (Union[Unset, int]): project id Example: 1.
        milestone_id (Union[Unset, int]): you can also provide a milestone_name(string) instead of milestone_id(integer)
            Example: 1.
        protocol_id (Union[Unset, int]): start experiment from protocol by providing the protocol id  Example: 1.
    """

    title: Union[Unset, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    milestone_id: Union[Unset, int] = UNSET
    protocol_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        project_id = self.project_id

        milestone_id = self.milestone_id

        protocol_id = self.protocol_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if milestone_id is not UNSET:
            field_dict["milestone_id"] = milestone_id
        if protocol_id is not UNSET:
            field_dict["protocol_id"] = protocol_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        project_id = d.pop("project_id", UNSET)

        milestone_id = d.pop("milestone_id", UNSET)

        protocol_id = d.pop("protocol_id", UNSET)

        experiment_base_request_item = cls(
            title=title,
            project_id=project_id,
            milestone_id=milestone_id,
            protocol_id=protocol_id,
        )

        experiment_base_request_item.additional_properties = d
        return experiment_base_request_item

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
