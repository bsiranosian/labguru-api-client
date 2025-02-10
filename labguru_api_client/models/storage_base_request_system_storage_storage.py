from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageBaseRequestSystemStorageStorage")


@_attrs_define
class StorageBaseRequestSystemStorageStorage:
    """
    Attributes:
        name (Union[Unset, str]): Name of the storage unit. Example: A large shelf.
        storage_type_id (Union[Unset, int]): The ID of the storage type.<br>Examples include: 1 (Room), 21 (Shelf), 61
            (Closet), 81 (Drawer), 111 (Cage), 120 (Refrigerator), 121 (Freezer), 201 (Cryo container), 251 (Slide Rack),
            322 (Rack), 321 (Other). Example: 21.
        description (Union[Unset, str]): description of the storage unit Example: Black shelf made of wood..
        temperature (Union[Unset, int]): temperature of the storage unit. Example: 7.
    """

    name: Union[Unset, str] = UNSET
    storage_type_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    temperature: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        storage_type_id = self.storage_type_id

        description = self.description

        temperature = self.temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if storage_type_id is not UNSET:
            field_dict["storage_type_id"] = storage_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        storage_type_id = d.pop("storage_type_id", UNSET)

        description = d.pop("description", UNSET)

        temperature = d.pop("temperature", UNSET)

        storage_base_request_system_storage_storage = cls(
            name=name,
            storage_type_id=storage_type_id,
            description=description,
            temperature=temperature,
        )

        storage_base_request_system_storage_storage.additional_properties = d
        return storage_base_request_system_storage_storage

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
