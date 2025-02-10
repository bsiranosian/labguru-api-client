from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyBaseRequestItem")


@_attrs_define
class CompanyBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): the company name Example: company name.
        address (Union[Unset, str]): address of the company Example: town&city.
        web (Union[Unset, str]): link to the company web page  Example: www.link.com.
        contact (Union[Unset, str]): contacts  Example: Mike: +973321434.
        email (Union[Unset, str]): email  Example: mail@gmail.com.
        fax (Union[Unset, str]): fax number  Example: +973321434.
        description (Union[Unset, str]): general description  Example: general description of the company.
    """

    name: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    web: Union[Unset, str] = UNSET
    contact: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        web = self.web

        contact = self.contact

        email = self.email

        fax = self.fax

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if web is not UNSET:
            field_dict["web"] = web
        if contact is not UNSET:
            field_dict["contact"] = contact
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        web = d.pop("web", UNSET)

        contact = d.pop("contact", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        description = d.pop("description", UNSET)

        company_base_request_item = cls(
            name=name,
            address=address,
            web=web,
            contact=contact,
            email=email,
            fax=fax,
            description=description,
        )

        company_base_request_item.additional_properties = d
        return company_base_request_item

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
