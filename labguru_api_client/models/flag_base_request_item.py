from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flag_base_request_item_color import FlagBaseRequestItemColor
from ..models.flag_base_request_item_icon import FlagBaseRequestItemIcon
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlagBaseRequestItem")


@_attrs_define
class FlagBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): Specifies the name of the flag
        icon (Union[Unset, FlagBaseRequestItemIcon]): The icon of the flag Example: star.
        color (Union[Unset, FlagBaseRequestItemColor]): The color of the flag Example: green.
        description (Union[Unset, str]): General description of the flag
    """

    title: Union[Unset, str] = UNSET
    icon: Union[Unset, FlagBaseRequestItemIcon] = UNSET
    color: Union[Unset, FlagBaseRequestItemColor] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        icon: Union[Unset, str] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.value

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if icon is not UNSET:
            field_dict["icon"] = icon
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, FlagBaseRequestItemIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = FlagBaseRequestItemIcon(_icon)

        _color = d.pop("color", UNSET)
        color: Union[Unset, FlagBaseRequestItemColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = FlagBaseRequestItemColor(_color)

        description = d.pop("description", UNSET)

        flag_base_request_item = cls(
            title=title,
            icon=icon,
            color=color,
            description=description,
        )

        flag_base_request_item.additional_properties = d
        return flag_base_request_item

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
