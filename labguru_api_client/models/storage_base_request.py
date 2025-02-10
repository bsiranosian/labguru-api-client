from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_base_request_system_storage_storage import StorageBaseRequestSystemStorageStorage


T = TypeVar("T", bound="StorageBaseRequest")


@_attrs_define
class StorageBaseRequest:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        system_storage_storage (Union[Unset, StorageBaseRequestSystemStorageStorage]):
    """

    token: str
    system_storage_storage: Union[Unset, "StorageBaseRequestSystemStorageStorage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        system_storage_storage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system_storage_storage, Unset):
            system_storage_storage = self.system_storage_storage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if system_storage_storage is not UNSET:
            field_dict["system_storage_storage"] = system_storage_storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.storage_base_request_system_storage_storage import StorageBaseRequestSystemStorageStorage

        d = src_dict.copy()
        token = d.pop("token")

        _system_storage_storage = d.pop("system_storage_storage", UNSET)
        system_storage_storage: Union[Unset, StorageBaseRequestSystemStorageStorage]
        if isinstance(_system_storage_storage, Unset):
            system_storage_storage = UNSET
        else:
            system_storage_storage = StorageBaseRequestSystemStorageStorage.from_dict(_system_storage_storage)

        storage_base_request = cls(
            token=token,
            system_storage_storage=system_storage_storage,
        )

        storage_base_request.additional_properties = d
        return storage_base_request

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
