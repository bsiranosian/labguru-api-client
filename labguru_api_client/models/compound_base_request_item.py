from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompoundBaseRequestItem")


@_attrs_define
class CompoundBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the compound Example: cmp-1.
        description (Union[Unset, str]): Updated description of the compound Example: General description.
        structure (Union[Unset, str]): Compound structure Example:
            C(=O)N1CCC(CCCC(=O)c2ccc(Cl)n(Cc3ncc(o3)-c3ccc(Cl)cc3)c2=O)CC1.
        cas (Union[Unset, str]): Compound CAS Example: cas.
        formula (Union[Unset, str]): Compound formula Example: H2O.
        molar_mass (Union[Unset, str]): Compound molar mass Example: molar mass.
        density (Union[Unset, str]): Compound density Example: density.
        boiling_point (Union[Unset, str]): Compound boiling point Example: 120.
        melting_point (Union[Unset, str]): Compound melting point Example: 30.
        hazards (Union[Unset, str]): Compound hazards Example: hazards.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    structure: Union[Unset, str] = UNSET
    cas: Union[Unset, str] = UNSET
    formula: Union[Unset, str] = UNSET
    molar_mass: Union[Unset, str] = UNSET
    density: Union[Unset, str] = UNSET
    boiling_point: Union[Unset, str] = UNSET
    melting_point: Union[Unset, str] = UNSET
    hazards: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        structure = self.structure

        cas = self.cas

        formula = self.formula

        molar_mass = self.molar_mass

        density = self.density

        boiling_point = self.boiling_point

        melting_point = self.melting_point

        hazards = self.hazards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if structure is not UNSET:
            field_dict["structure"] = structure
        if cas is not UNSET:
            field_dict["cas"] = cas
        if formula is not UNSET:
            field_dict["formula"] = formula
        if molar_mass is not UNSET:
            field_dict["molar_mass"] = molar_mass
        if density is not UNSET:
            field_dict["density"] = density
        if boiling_point is not UNSET:
            field_dict["boiling_point"] = boiling_point
        if melting_point is not UNSET:
            field_dict["melting_point"] = melting_point
        if hazards is not UNSET:
            field_dict["hazards"] = hazards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        structure = d.pop("structure", UNSET)

        cas = d.pop("cas", UNSET)

        formula = d.pop("formula", UNSET)

        molar_mass = d.pop("molar_mass", UNSET)

        density = d.pop("density", UNSET)

        boiling_point = d.pop("boiling_point", UNSET)

        melting_point = d.pop("melting_point", UNSET)

        hazards = d.pop("hazards", UNSET)

        compound_base_request_item = cls(
            name=name,
            description=description,
            structure=structure,
            cas=cas,
            formula=formula,
            molar_mass=molar_mass,
            density=density,
            boiling_point=boiling_point,
            melting_point=melting_point,
            hazards=hazards,
        )

        compound_base_request_item.additional_properties = d
        return compound_base_request_item

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
