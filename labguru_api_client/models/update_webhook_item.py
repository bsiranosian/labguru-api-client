from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookItem")


@_attrs_define
class UpdateWebhookItem:
    """
    Attributes:
        trigger_key (Union[Unset, str]): trigger key Example: knowledgebase_document.signed.
        active (Union[Unset, int]): 1/0 Example: 1.
        url (Union[Unset, str]): url Example: https://prod-flow.labguru.com/flows/1234567/flow_runs.json.
    """

    trigger_key: Union[Unset, str] = UNSET
    active: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_key = self.trigger_key

        active = self.active

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trigger_key is not UNSET:
            field_dict["trigger_key"] = trigger_key
        if active is not UNSET:
            field_dict["active"] = active
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        trigger_key = d.pop("trigger_key", UNSET)

        active = d.pop("active", UNSET)

        url = d.pop("url", UNSET)

        update_webhook_item = cls(
            trigger_key=trigger_key,
            active=active,
            url=url,
        )

        update_webhook_item.additional_properties = d
        return update_webhook_item

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
