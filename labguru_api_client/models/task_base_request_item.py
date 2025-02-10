from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskBaseRequestItem")


@_attrs_define
class TaskBaseRequestItem:
    """
    Attributes:
        name (str): The name of the Task Example: Task 1.
        start_date (Union[Unset, str]): Start Date (yyyy-mm-dd) Example: 2021-02-03.
        assigned_to (Union[Unset, int]): id of assigner Example: 1.
        description (Union[Unset, str]): Description of the task Example: General task description.
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        notify_at (Union[Unset, str]): notification date & time (yyyy-mm-dd) Example: 2021-03-04.
    """

    name: str
    start_date: Union[Unset, str] = UNSET
    assigned_to: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    notify_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start_date = self.start_date

        assigned_to = self.assigned_to

        description = self.description

        owner_id = self.owner_id

        notify_at = self.notify_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if assigned_to is not UNSET:
            field_dict["assigned_to"] = assigned_to
        if description is not UNSET:
            field_dict["description"] = description
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if notify_at is not UNSET:
            field_dict["notify_at"] = notify_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        start_date = d.pop("start_date", UNSET)

        assigned_to = d.pop("assigned_to", UNSET)

        description = d.pop("description", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        notify_at = d.pop("notify_at", UNSET)

        task_base_request_item = cls(
            name=name,
            start_date=start_date,
            assigned_to=assigned_to,
            description=description,
            owner_id=owner_id,
            notify_at=notify_at,
        )

        task_base_request_item.additional_properties = d
        return task_base_request_item

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
