from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkBaseRequestItem")


@_attrs_define
class LinkBaseRequestItem:
    """
    Attributes:
        source_id (Union[Unset, int]): ID of the source item Example: 126.
        source_type (Union[Unset, str]): Type of the source item Example: Biocollections::Plasmid.
        target_id (Union[Unset, int]): ID of the target item Example: 96.
        target_type (Union[Unset, str]): Type of the target item Example: Biocollections::Plasmid.
        source_uuid (Union[Unset, str]): UUID of the source item Example: 4d7eafcd-8d65-49fd-8e96-091edbbef980.
        target_uuid (Union[Unset, str]): UUID of the target item Example: 53cca961-8d6b-4f34-ba6e-cfa8e393b2a9.
    """

    source_id: Union[Unset, int] = UNSET
    source_type: Union[Unset, str] = UNSET
    target_id: Union[Unset, int] = UNSET
    target_type: Union[Unset, str] = UNSET
    source_uuid: Union[Unset, str] = UNSET
    target_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_id = self.source_id

        source_type = self.source_type

        target_id = self.target_id

        target_type = self.target_type

        source_uuid = self.source_uuid

        target_uuid = self.target_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if source_uuid is not UNSET:
            field_dict["source_uuid"] = source_uuid
        if target_uuid is not UNSET:
            field_dict["target_uuid"] = target_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        source_id = d.pop("source_id", UNSET)

        source_type = d.pop("source_type", UNSET)

        target_id = d.pop("target_id", UNSET)

        target_type = d.pop("target_type", UNSET)

        source_uuid = d.pop("source_uuid", UNSET)

        target_uuid = d.pop("target_uuid", UNSET)

        link_base_request_item = cls(
            source_id=source_id,
            source_type=source_type,
            target_id=target_id,
            target_type=target_type,
            source_uuid=source_uuid,
            target_uuid=target_uuid,
        )

        link_base_request_item.additional_properties = d
        return link_base_request_item

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
