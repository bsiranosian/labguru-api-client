from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFormElement")


@_attrs_define
class UpdateFormElement:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        form_json (Union[Unset, str]): A JSON string containing key-value pairs that specify updates to the form fields.
                              Each key corresponds to a form field name and the value specifies the new content for that
            field. Example: {'Field Name': 'Field Content'}.
    """

    token: str
    form_json: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        form_json = self.form_json

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if form_json is not UNSET:
            field_dict["form_json"] = form_json

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        form_json = d.pop("form_json", UNSET)

        update_form_element = cls(
            token=token,
            form_json=form_json,
        )

        update_form_element.additional_properties = d
        return update_form_element

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
