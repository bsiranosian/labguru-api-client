from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiV1BiocollectionNameIdBodyItem")


@_attrs_define
class PutApiV1BiocollectionNameIdBodyItem:
    """
    Attributes:
        title (Union[Unset, str]): the item title to add parent to  Example: child.
        parents_uuid (Union[Unset, list[str]]):
    """

    title: Union[Unset, str] = UNSET
    parents_uuid: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        parents_uuid: Union[Unset, list[str]] = UNSET
        if not isinstance(self.parents_uuid, Unset):
            parents_uuid = self.parents_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if parents_uuid is not UNSET:
            field_dict["parents_uuid"] = parents_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        parents_uuid = cast(list[str], d.pop("parents_uuid", UNSET))

        put_api_v1_biocollection_name_id_body_item = cls(
            title=title,
            parents_uuid=parents_uuid,
        )

        put_api_v1_biocollection_name_id_body_item.additional_properties = d
        return put_api_v1_biocollection_name_id_body_item

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
