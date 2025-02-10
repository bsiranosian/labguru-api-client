from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectBaseRequestItem")


@_attrs_define
class ProjectBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): The name of the project Example: project-name.
        description (Union[Unset, str]): Description of the project Example: General description.
        start_date (Union[Unset, str]): Start Date (yyyy-mm-dd) Example: 2021-02-03.
        closed (Union[Unset, bool]): Archived/Active project flag
        status (Union[Unset, str]): Status Example: Project Closed At 2019-07-22 by John Doe.
        owner_id (Union[Unset, int]): ID of the owner (default: your member id) Example: Your member id.
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    closed: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        start_date = self.start_date

        closed = self.closed

        status = self.status

        owner_id = self.owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if closed is not UNSET:
            field_dict["closed"] = closed
        if status is not UNSET:
            field_dict["status"] = status
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        start_date = d.pop("start_date", UNSET)

        closed = d.pop("closed", UNSET)

        status = d.pop("status", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        project_base_request_item = cls(
            title=title,
            description=description,
            start_date=start_date,
            closed=closed,
            status=status,
            owner_id=owner_id,
        )

        project_base_request_item.additional_properties = d
        return project_base_request_item

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
