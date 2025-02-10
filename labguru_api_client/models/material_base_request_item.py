from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaterialBaseRequestItem")


@_attrs_define
class MaterialBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): Material name Example: Material.
        company_id (Union[Unset, int]): [required] - in case material is commercial Example: 31.
        produce_by (Union[Unset, str]): [required] - in case material is non commercial Example: value.
        description (Union[Unset, str]): description Example: General description.
        cas_number (Union[Unset, int]): CAS Registry Number Example: 58.
        mw (Union[Unset, str]): mw Example: 1.
        web (Union[Unset, str]): url Example: https://my.labguru.com.
        materialtype_id (Union[Unset, int]): the material type id Example: 1.
        units (Union[Unset, str]): units Example: 20.
        price (Union[Unset, float]): price Example: 100.60.
        currency (Union[Unset, int]): 0 = NIS, 1 = DOLLAR, 2 = EURO, 3 = POUND, 4 = NOK  Example: 4.
    """

    name: Union[Unset, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    produce_by: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    cas_number: Union[Unset, int] = UNSET
    mw: Union[Unset, str] = UNSET
    web: Union[Unset, str] = UNSET
    materialtype_id: Union[Unset, int] = UNSET
    units: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    currency: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        company_id = self.company_id

        produce_by = self.produce_by

        description = self.description

        cas_number = self.cas_number

        mw = self.mw

        web = self.web

        materialtype_id = self.materialtype_id

        units = self.units

        price = self.price

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if produce_by is not UNSET:
            field_dict["produce_by"] = produce_by
        if description is not UNSET:
            field_dict["description"] = description
        if cas_number is not UNSET:
            field_dict["cas_number"] = cas_number
        if mw is not UNSET:
            field_dict["mw"] = mw
        if web is not UNSET:
            field_dict["web"] = web
        if materialtype_id is not UNSET:
            field_dict["materialtype_id"] = materialtype_id
        if units is not UNSET:
            field_dict["units"] = units
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        company_id = d.pop("company_id", UNSET)

        produce_by = d.pop("produce_by", UNSET)

        description = d.pop("description", UNSET)

        cas_number = d.pop("cas_number", UNSET)

        mw = d.pop("mw", UNSET)

        web = d.pop("web", UNSET)

        materialtype_id = d.pop("materialtype_id", UNSET)

        units = d.pop("units", UNSET)

        price = d.pop("price", UNSET)

        currency = d.pop("currency", UNSET)

        material_base_request_item = cls(
            name=name,
            company_id=company_id,
            produce_by=produce_by,
            description=description,
            cas_number=cas_number,
            mw=mw,
            web=web,
            materialtype_id=materialtype_id,
            units=units,
            price=price,
            currency=currency,
        )

        material_base_request_item.additional_properties = d
        return material_base_request_item

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
