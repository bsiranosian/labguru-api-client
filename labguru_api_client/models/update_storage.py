from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_base_request_system_storage_storage import StorageBaseRequestSystemStorageStorage
    from ..models.update_storage_item import UpdateStorageItem


T = TypeVar("T", bound="UpdateStorage")


@_attrs_define
class UpdateStorage:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        system_storage_storage (Union[Unset, StorageBaseRequestSystemStorageStorage]):
        item (Union[Unset, UpdateStorageItem]):
    """

    token: str
    system_storage_storage: Union[Unset, "StorageBaseRequestSystemStorageStorage"] = UNSET
    item: Union[Unset, "UpdateStorageItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        system_storage_storage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system_storage_storage, Unset):
            system_storage_storage = self.system_storage_storage.to_dict()

        item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if system_storage_storage is not UNSET:
            field_dict["system_storage_storage"] = system_storage_storage
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.storage_base_request_system_storage_storage import StorageBaseRequestSystemStorageStorage
        from ..models.update_storage_item import UpdateStorageItem

        d = src_dict.copy()
        token = d.pop("token")

        _system_storage_storage = d.pop("system_storage_storage", UNSET)
        system_storage_storage: Union[Unset, StorageBaseRequestSystemStorageStorage]
        if isinstance(_system_storage_storage, Unset):
            system_storage_storage = UNSET
        else:
            system_storage_storage = StorageBaseRequestSystemStorageStorage.from_dict(_system_storage_storage)

        _item = d.pop("item", UNSET)
        item: Union[Unset, UpdateStorageItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = UpdateStorageItem.from_dict(_item)

        update_storage = cls(
            token=token,
            system_storage_storage=system_storage_storage,
            item=item,
        )

        update_storage.additional_properties = d
        return update_storage

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
