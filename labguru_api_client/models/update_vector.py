from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateVector")


@_attrs_define
class UpdateVector:
    """
    Attributes:
        token (Union[Unset, str]):  Example: YOUR TOKEN IS HERE.
        dataset_id (Union[Unset, str]): the dataset id Example: 3.
        vector_data (Union[Unset, str]): fields must be same as column headers in the dataset - {"data_header":
            "item_name"} Example: {'column1': 'value1', 'column2': 'value2'}.
    """

    token: Union[Unset, str] = UNSET
    dataset_id: Union[Unset, str] = UNSET
    vector_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        dataset_id = self.dataset_id

        vector_data = self.vector_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if vector_data is not UNSET:
            field_dict["vector_data"] = vector_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        dataset_id = d.pop("dataset_id", UNSET)

        vector_data = d.pop("vector_data", UNSET)

        update_vector = cls(
            token=token,
            dataset_id=dataset_id,
            vector_data=vector_data,
        )

        update_vector.additional_properties = d
        return update_vector

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
