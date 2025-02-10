import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockBaseRequestItem")


@_attrs_define
class StockBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): the stock name  Example: Stocky.
        storage_id (Union[Unset, int]): type of storages: 1 - Room, 21 - Shelf, 61 - Closet, 81 - Drawer, 111 - Cage,
            120 - Refrigerator ,121 - Freezer, 181 - Rack Cell , 201 - Cryo container, 251 - Slide Rack, 261 - Rack Cell,
            322 - Rack, 323 - Rack Cell, 321 - Other Example: 1.
        storage_type (Union[Unset, str]): storage class name - [Box - System::Storage::Box] [all other storages type -
            System::Storage::Storage]  Example: System::Storage::Storage.
        stockable_type (Union[Unset, str]): class name of the stockable item type Example: Biocollections::Antibody.
        stockable_id (Union[Unset, int]): stockable item id Example: 1.
        location_in_box (Union[Unset, int]): if storage is grid box, indicates numerical location in box Example: 1.
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        expiration_date (Union[Unset, datetime.date]): in the following format: yyyy-mm-dd  Example: 2023-11-21.
        lot (Union[Unset, str]): number of batch Example: 103.
        description (Union[Unset, str]): general description Example: general description.
        barcode (Union[Unset, str]): barcode  Example: 123456.
        stored_by (Union[Unset, int]): member id Example: MEMBER_ID.
        concentration (Union[Unset, str]): concentration Example: 100.
        concentration_prefix (Union[Unset, str]): x10^/E^ Example: E^.
        concentration_unit_id (Union[Unset, int]): 9-mg/mL, 10-g/L, 11-M, 12-mM, 13-µM, 14-µg/mL, 15-ng/µL, 16-ratio,
            17-%, 18-g/mL Example: 9.
        concentration_exponent (Union[Unset, str]): concentration exponent Example: 2.
        concentration_remarks (Union[Unset, str]): concentration remarks Example: concentration remarks.
        volume (Union[Unset, str]): volume Example: 150.
        volume_prefix (Union[Unset, str]): x10^/E^ Example: E^.
        volume_unit_id (Union[Unset, int]): 6-L, 7-mL, 8-µL Example: 7.
        volume_exponent (Union[Unset, str]): volume exponent Example: 4.
        volume_remarks (Union[Unset, str]): volume remarks Example: volume remarks.
        weight (Union[Unset, str]): weight Example: 150.
        weight_prefix (Union[Unset, str]): x10^/E^ Example: E^.
        weight_unit_id (Union[Unset, int]): 1 -Kg, 2-g, 3-mg, 4-µg, 5-ng Example: 1.
        weight_exponent (Union[Unset, str]): weight exponent Example: 25.
        weight_remarks (Union[Unset, str]): weight remarks Example: weight remarks.
    """

    name: Union[Unset, str] = UNSET
    storage_id: Union[Unset, int] = UNSET
    storage_type: Union[Unset, str] = UNSET
    stockable_type: Union[Unset, str] = UNSET
    stockable_id: Union[Unset, int] = UNSET
    location_in_box: Union[Unset, int] = UNSET
    owner_id: Union[Unset, int] = UNSET
    expiration_date: Union[Unset, datetime.date] = UNSET
    lot: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    barcode: Union[Unset, str] = UNSET
    stored_by: Union[Unset, int] = UNSET
    concentration: Union[Unset, str] = UNSET
    concentration_prefix: Union[Unset, str] = UNSET
    concentration_unit_id: Union[Unset, int] = UNSET
    concentration_exponent: Union[Unset, str] = UNSET
    concentration_remarks: Union[Unset, str] = UNSET
    volume: Union[Unset, str] = UNSET
    volume_prefix: Union[Unset, str] = UNSET
    volume_unit_id: Union[Unset, int] = UNSET
    volume_exponent: Union[Unset, str] = UNSET
    volume_remarks: Union[Unset, str] = UNSET
    weight: Union[Unset, str] = UNSET
    weight_prefix: Union[Unset, str] = UNSET
    weight_unit_id: Union[Unset, int] = UNSET
    weight_exponent: Union[Unset, str] = UNSET
    weight_remarks: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        storage_id = self.storage_id

        storage_type = self.storage_type

        stockable_type = self.stockable_type

        stockable_id = self.stockable_id

        location_in_box = self.location_in_box

        owner_id = self.owner_id

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        lot = self.lot

        description = self.description

        barcode = self.barcode

        stored_by = self.stored_by

        concentration = self.concentration

        concentration_prefix = self.concentration_prefix

        concentration_unit_id = self.concentration_unit_id

        concentration_exponent = self.concentration_exponent

        concentration_remarks = self.concentration_remarks

        volume = self.volume

        volume_prefix = self.volume_prefix

        volume_unit_id = self.volume_unit_id

        volume_exponent = self.volume_exponent

        volume_remarks = self.volume_remarks

        weight = self.weight

        weight_prefix = self.weight_prefix

        weight_unit_id = self.weight_unit_id

        weight_exponent = self.weight_exponent

        weight_remarks = self.weight_remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if storage_type is not UNSET:
            field_dict["storage_type"] = storage_type
        if stockable_type is not UNSET:
            field_dict["stockable_type"] = stockable_type
        if stockable_id is not UNSET:
            field_dict["stockable_id"] = stockable_id
        if location_in_box is not UNSET:
            field_dict["location_in_box"] = location_in_box
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if lot is not UNSET:
            field_dict["lot"] = lot
        if description is not UNSET:
            field_dict["description"] = description
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if stored_by is not UNSET:
            field_dict["stored_by"] = stored_by
        if concentration is not UNSET:
            field_dict["concentration"] = concentration
        if concentration_prefix is not UNSET:
            field_dict["concentration_prefix"] = concentration_prefix
        if concentration_unit_id is not UNSET:
            field_dict["concentration_unit_id"] = concentration_unit_id
        if concentration_exponent is not UNSET:
            field_dict["concentration_exponent"] = concentration_exponent
        if concentration_remarks is not UNSET:
            field_dict["concentration_remarks"] = concentration_remarks
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_prefix is not UNSET:
            field_dict["volume_prefix"] = volume_prefix
        if volume_unit_id is not UNSET:
            field_dict["volume_unit_id"] = volume_unit_id
        if volume_exponent is not UNSET:
            field_dict["volume_exponent"] = volume_exponent
        if volume_remarks is not UNSET:
            field_dict["volume_remarks"] = volume_remarks
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_prefix is not UNSET:
            field_dict["weight_prefix"] = weight_prefix
        if weight_unit_id is not UNSET:
            field_dict["weight_unit_id"] = weight_unit_id
        if weight_exponent is not UNSET:
            field_dict["weight_exponent"] = weight_exponent
        if weight_remarks is not UNSET:
            field_dict["weight_remarks"] = weight_remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        storage_id = d.pop("storage_id", UNSET)

        storage_type = d.pop("storage_type", UNSET)

        stockable_type = d.pop("stockable_type", UNSET)

        stockable_id = d.pop("stockable_id", UNSET)

        location_in_box = d.pop("location_in_box", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        _expiration_date = d.pop("expiration_date", UNSET)
        expiration_date: Union[Unset, datetime.date]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date).date()

        lot = d.pop("lot", UNSET)

        description = d.pop("description", UNSET)

        barcode = d.pop("barcode", UNSET)

        stored_by = d.pop("stored_by", UNSET)

        concentration = d.pop("concentration", UNSET)

        concentration_prefix = d.pop("concentration_prefix", UNSET)

        concentration_unit_id = d.pop("concentration_unit_id", UNSET)

        concentration_exponent = d.pop("concentration_exponent", UNSET)

        concentration_remarks = d.pop("concentration_remarks", UNSET)

        volume = d.pop("volume", UNSET)

        volume_prefix = d.pop("volume_prefix", UNSET)

        volume_unit_id = d.pop("volume_unit_id", UNSET)

        volume_exponent = d.pop("volume_exponent", UNSET)

        volume_remarks = d.pop("volume_remarks", UNSET)

        weight = d.pop("weight", UNSET)

        weight_prefix = d.pop("weight_prefix", UNSET)

        weight_unit_id = d.pop("weight_unit_id", UNSET)

        weight_exponent = d.pop("weight_exponent", UNSET)

        weight_remarks = d.pop("weight_remarks", UNSET)

        stock_base_request_item = cls(
            name=name,
            storage_id=storage_id,
            storage_type=storage_type,
            stockable_type=stockable_type,
            stockable_id=stockable_id,
            location_in_box=location_in_box,
            owner_id=owner_id,
            expiration_date=expiration_date,
            lot=lot,
            description=description,
            barcode=barcode,
            stored_by=stored_by,
            concentration=concentration,
            concentration_prefix=concentration_prefix,
            concentration_unit_id=concentration_unit_id,
            concentration_exponent=concentration_exponent,
            concentration_remarks=concentration_remarks,
            volume=volume,
            volume_prefix=volume_prefix,
            volume_unit_id=volume_unit_id,
            volume_exponent=volume_exponent,
            volume_remarks=volume_remarks,
            weight=weight,
            weight_prefix=weight_prefix,
            weight_unit_id=weight_unit_id,
            weight_exponent=weight_exponent,
            weight_remarks=weight_remarks,
        )

        stock_base_request_item.additional_properties = d
        return stock_base_request_item

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
