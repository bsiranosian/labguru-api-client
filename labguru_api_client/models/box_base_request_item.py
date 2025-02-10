from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BoxBaseRequestItem")


@_attrs_define
class BoxBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): the box name  Example: A box.
        rows (Union[Unset, str]): number of rows Example: 5.
        cols (Union[Unset, int]): number of columns Example: 5.
        box_type (Union[Unset, int]): one of the following: [["Primer", 0], ["General", -1], ["Tube", -1], ["Seed", -2],
            ["Fly", -3], ["Bacterium", -4], ["Bacteria", -4], ["CellLine", -5], ["Cell Line", -5], ["Cellline", -5],
            ["Tissue", -6], ["Antibody", -7], ["Plasmid", -8], ["Glycerol", -9], ["Enzyme", -10], ["Consumable", -11],
            ["Yeast", -12], ["Fungus", -13], ["Virus", -14], ["Protein", -15], ["Lipid", -16], ["Worm", -17], ["Sequence",
            -18], ["Zebrafish", -19], ["Gene", -20], ["Compound", -21]]
        color (Union[Unset, str]): ["pink", "red", "orange", "yellow", "beige", "white", "blue", "purple", "green",
            "brown", "gray", "black"] Example: blue.
        shared (Union[Unset, bool]): Personal - false/ shared - true(default) Example: 1.
        barcode (Union[Unset, str]): the barcode of the box Example: 1234ABCD.
    """

    name: Union[Unset, str] = UNSET
    rows: Union[Unset, str] = UNSET
    cols: Union[Unset, int] = UNSET
    box_type: Union[Unset, int] = UNSET
    color: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    barcode: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        rows = self.rows

        cols = self.cols

        box_type = self.box_type

        color = self.color

        shared = self.shared

        barcode = self.barcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if rows is not UNSET:
            field_dict["rows"] = rows
        if cols is not UNSET:
            field_dict["cols"] = cols
        if box_type is not UNSET:
            field_dict["box_type"] = box_type
        if color is not UNSET:
            field_dict["color"] = color
        if shared is not UNSET:
            field_dict["shared"] = shared
        if barcode is not UNSET:
            field_dict["barcode"] = barcode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        rows = d.pop("rows", UNSET)

        cols = d.pop("cols", UNSET)

        box_type = d.pop("box_type", UNSET)

        color = d.pop("color", UNSET)

        shared = d.pop("shared", UNSET)

        barcode = d.pop("barcode", UNSET)

        box_base_request_item = cls(
            name=name,
            rows=rows,
            cols=cols,
            box_type=box_type,
            color=color,
            shared=shared,
            barcode=barcode,
        )

        box_base_request_item.additional_properties = d
        return box_base_request_item

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
