from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MoveSection")


@_attrs_define
class MoveSection:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        container_id (int): The id of the container Example: 347.
        container_type (str): The container type of the section Default: 'Projects::Experiment'.
        list_ (list[int]): An array of section IDs.<br>
                            The order of IDs in this list defines the new arrangement of sections on the page Example: [110,
            111].
    """

    token: str
    container_id: int
    list_: list[int]
    container_type: str = "Projects::Experiment"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        container_id = self.container_id

        container_type = self.container_type

        list_ = self.list_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "container_id": container_id,
                "container_type": container_type,
                "list": list_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        container_id = d.pop("container_id")

        container_type = d.pop("container_type")

        list_ = cast(list[int], d.pop("list"))

        move_section = cls(
            token=token,
            container_id=container_id,
            container_type=container_type,
            list_=list_,
        )

        move_section.additional_properties = d
        return move_section

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
