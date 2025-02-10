import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventBaseRequestItem")


@_attrs_define
class EventBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): event title Example: Lab meeting.
        start_date (Union[Unset, datetime.date]): the event start date Example: 2021-05-23 06:22:00.
        end_date (Union[Unset, datetime.date]): the event end date Example: 2021-07-23 06:22:00.
        description (Union[Unset, str]):  text description for this event Example: very important meeting.
        notify_members (Union[Unset, str]): who should be notified regarding the event: notify only me =[1], notify all
            participants = [-1], none =[0] Example: [0].
        notify_at (Union[Unset, datetime.date]): when to notify about the event Example: 2020-05-23 06:22:00.
        is_fullday_event (Union[Unset, bool]): true/false Example: True.
        repeats (Union[Unset, int]): 1/0 Example: 1.
        repeat_frame (Union[Unset, str]): the time frame which the event will be repeated at - Never, days, weeks,
            months Example: Never.
        eventable_id (Union[Unset, int]): the equipment id which the event is related to Example: 12.
        eventable_type (Union[Unset, str]): equipment item class name - System::Instrument Example: System::Instrument.
    """

    name: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    description: Union[Unset, str] = UNSET
    notify_members: Union[Unset, str] = UNSET
    notify_at: Union[Unset, datetime.date] = UNSET
    is_fullday_event: Union[Unset, bool] = UNSET
    repeats: Union[Unset, int] = UNSET
    repeat_frame: Union[Unset, str] = UNSET
    eventable_id: Union[Unset, int] = UNSET
    eventable_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        description = self.description

        notify_members = self.notify_members

        notify_at: Union[Unset, str] = UNSET
        if not isinstance(self.notify_at, Unset):
            notify_at = self.notify_at.isoformat()

        is_fullday_event = self.is_fullday_event

        repeats = self.repeats

        repeat_frame = self.repeat_frame

        eventable_id = self.eventable_id

        eventable_type = self.eventable_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if description is not UNSET:
            field_dict["description"] = description
        if notify_members is not UNSET:
            field_dict["notify_members"] = notify_members
        if notify_at is not UNSET:
            field_dict["notify_at"] = notify_at
        if is_fullday_event is not UNSET:
            field_dict["is_fullday_event"] = is_fullday_event
        if repeats is not UNSET:
            field_dict["repeats"] = repeats
        if repeat_frame is not UNSET:
            field_dict["repeat_frame"] = repeat_frame
        if eventable_id is not UNSET:
            field_dict["eventable_id"] = eventable_id
        if eventable_type is not UNSET:
            field_dict["eventable_type"] = eventable_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        description = d.pop("description", UNSET)

        notify_members = d.pop("notify_members", UNSET)

        _notify_at = d.pop("notify_at", UNSET)
        notify_at: Union[Unset, datetime.date]
        if isinstance(_notify_at, Unset):
            notify_at = UNSET
        else:
            notify_at = isoparse(_notify_at).date()

        is_fullday_event = d.pop("is_fullday_event", UNSET)

        repeats = d.pop("repeats", UNSET)

        repeat_frame = d.pop("repeat_frame", UNSET)

        eventable_id = d.pop("eventable_id", UNSET)

        eventable_type = d.pop("eventable_type", UNSET)

        event_base_request_item = cls(
            name=name,
            start_date=start_date,
            end_date=end_date,
            description=description,
            notify_members=notify_members,
            notify_at=notify_at,
            is_fullday_event=is_fullday_event,
            repeats=repeats,
            repeat_frame=repeat_frame,
            eventable_id=eventable_id,
            eventable_type=eventable_type,
        )

        event_base_request_item.additional_properties = d
        return event_base_request_item

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
