from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LipidBaseRequestItem")


@_attrs_define
class LipidBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the lipid
        owner_id (Union[Unset, int]): ID of the owner (default: your member id) Example: Your member id.
        alternative_name (Union[Unset, str]): Any alternative name by which the lipid may be known
        molecular_formula (Union[Unset, str]): The molecular formula of the lipid
        molecular_weight (Union[Unset, str]): Molecular weight of the lipid
        cas_number (Union[Unset, str]): The Chemical Abstracts Service number
        stock_solution_prep (Union[Unset, str]): Media/solution
        solubility (Union[Unset, str]): Solubility information
        conditions_for_use (Union[Unset, str]): Recommended conditions under which the lipid should be used
        conditions_for_storage (Union[Unset, str]): Guidelines for proper storage of the lipid
        safety_information (Union[Unset, str]): Safety guidelines and hazard information related to the lipid
        impurities (Union[Unset, str]): Details of known impurities found in the lipid sample
        source (Union[Unset, str]): The origin of the lipid
        description (Union[Unset, str]): Detailed description of the lipid
    """

    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    molecular_formula: Union[Unset, str] = UNSET
    molecular_weight: Union[Unset, str] = UNSET
    cas_number: Union[Unset, str] = UNSET
    stock_solution_prep: Union[Unset, str] = UNSET
    solubility: Union[Unset, str] = UNSET
    conditions_for_use: Union[Unset, str] = UNSET
    conditions_for_storage: Union[Unset, str] = UNSET
    safety_information: Union[Unset, str] = UNSET
    impurities: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_id = self.owner_id

        alternative_name = self.alternative_name

        molecular_formula = self.molecular_formula

        molecular_weight = self.molecular_weight

        cas_number = self.cas_number

        stock_solution_prep = self.stock_solution_prep

        solubility = self.solubility

        conditions_for_use = self.conditions_for_use

        conditions_for_storage = self.conditions_for_storage

        safety_information = self.safety_information

        impurities = self.impurities

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if molecular_formula is not UNSET:
            field_dict["molecular_formula"] = molecular_formula
        if molecular_weight is not UNSET:
            field_dict["molecular_weight"] = molecular_weight
        if cas_number is not UNSET:
            field_dict["cas_number"] = cas_number
        if stock_solution_prep is not UNSET:
            field_dict["stock_solution_prep"] = stock_solution_prep
        if solubility is not UNSET:
            field_dict["solubility"] = solubility
        if conditions_for_use is not UNSET:
            field_dict["conditions_for_use"] = conditions_for_use
        if conditions_for_storage is not UNSET:
            field_dict["conditions_for_storage"] = conditions_for_storage
        if safety_information is not UNSET:
            field_dict["safety_information"] = safety_information
        if impurities is not UNSET:
            field_dict["impurities"] = impurities
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        molecular_formula = d.pop("molecular_formula", UNSET)

        molecular_weight = d.pop("molecular_weight", UNSET)

        cas_number = d.pop("cas_number", UNSET)

        stock_solution_prep = d.pop("stock_solution_prep", UNSET)

        solubility = d.pop("solubility", UNSET)

        conditions_for_use = d.pop("conditions_for_use", UNSET)

        conditions_for_storage = d.pop("conditions_for_storage", UNSET)

        safety_information = d.pop("safety_information", UNSET)

        impurities = d.pop("impurities", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        lipid_base_request_item = cls(
            name=name,
            owner_id=owner_id,
            alternative_name=alternative_name,
            molecular_formula=molecular_formula,
            molecular_weight=molecular_weight,
            cas_number=cas_number,
            stock_solution_prep=stock_solution_prep,
            solubility=solubility,
            conditions_for_use=conditions_for_use,
            conditions_for_storage=conditions_for_storage,
            safety_information=safety_information,
            impurities=impurities,
            source=source,
            description=description,
        )

        lipid_base_request_item.additional_properties = d
        return lipid_base_request_item

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
