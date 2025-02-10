from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1ExperimentsIdSetFlagAsResponse200Flag")


@_attrs_define
class PostApiV1ExperimentsIdSetFlagAsResponse200Flag:
    """
    Attributes:
        id (Union[Unset, int]): The ID of the flag
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        color (Union[Unset, str]):
        icon (Union[Unset, str]):
        active (Union[Unset, bool]):
        default (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        color = self.color

        icon = self.icon

        active = self.active

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if active is not UNSET:
            field_dict["active"] = active
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        active = d.pop("active", UNSET)

        default = d.pop("default", UNSET)

        post_api_v1_experiments_id_set_flag_as_response_200_flag = cls(
            id=id,
            title=title,
            description=description,
            color=color,
            icon=icon,
            active=active,
            default=default,
        )

        post_api_v1_experiments_id_set_flag_as_response_200_flag.additional_properties = d
        return post_api_v1_experiments_id_set_flag_as_response_200_flag

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
