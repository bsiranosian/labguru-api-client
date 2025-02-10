from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteBaseRequestItem")


@_attrs_define
class NoteBaseRequestItem:
    """
    Attributes:
        title (str): the note title  Example: lab TDL.
        project_id (int): the project id to add note to Example: 1.
        body (Union[Unset, str]): body description of the note Example: the note body.
    """

    title: str
    project_id: int
    body: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        project_id = self.project_id

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "project_id": project_id,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        project_id = d.pop("project_id")

        body = d.pop("body", UNSET)

        note_base_request_item = cls(
            title=title,
            project_id=project_id,
            body=body,
        )

        note_base_request_item.additional_properties = d
        return note_base_request_item

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
