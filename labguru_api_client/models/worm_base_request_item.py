from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WormBaseRequestItem")


@_attrs_define
class WormBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the worm
        alternative_name (Union[Unset, str]): An alternative name for the worm
        gene_id (Union[Unset, int]): An ID reference to a gene from your labguru genes collection
        source (Union[Unset, str]): Origin of the worm
        genotype (Union[Unset, str]): Genetic constitution of the worm
        phenotype (Union[Unset, str]): Observable physical or biochemical characteristics of the worm
        mutagen (Union[Unset, str]): The agent used to induce mutations in the worm
        growth_conditions (Union[Unset, str]): Specific conditions under which the worm is maintained
        outcrossed (Union[Unset, int]): Number of times the worm strain has been outcrossed with another
        made_by (Union[Unset, str]): researcher name input
        dauer_defective (Union[Unset, bool]): Indicates whether the worm is defective in entering or exiting the dauer
            stage,
                                with '1' for yes and '0' for no.
        description (Union[Unset, str]): Description of the worm
    """

    name: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    gene_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    genotype: Union[Unset, str] = UNSET
    phenotype: Union[Unset, str] = UNSET
    mutagen: Union[Unset, str] = UNSET
    growth_conditions: Union[Unset, str] = UNSET
    outcrossed: Union[Unset, int] = UNSET
    made_by: Union[Unset, str] = UNSET
    dauer_defective: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alternative_name = self.alternative_name

        gene_id = self.gene_id

        source = self.source

        genotype = self.genotype

        phenotype = self.phenotype

        mutagen = self.mutagen

        growth_conditions = self.growth_conditions

        outcrossed = self.outcrossed

        made_by = self.made_by

        dauer_defective = self.dauer_defective

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if gene_id is not UNSET:
            field_dict["gene_id"] = gene_id
        if source is not UNSET:
            field_dict["source"] = source
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
        if mutagen is not UNSET:
            field_dict["mutagen"] = mutagen
        if growth_conditions is not UNSET:
            field_dict["growth_conditions"] = growth_conditions
        if outcrossed is not UNSET:
            field_dict["outcrossed"] = outcrossed
        if made_by is not UNSET:
            field_dict["made_by"] = made_by
        if dauer_defective is not UNSET:
            field_dict["dauer_defective"] = dauer_defective
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        gene_id = d.pop("gene_id", UNSET)

        source = d.pop("source", UNSET)

        genotype = d.pop("genotype", UNSET)

        phenotype = d.pop("phenotype", UNSET)

        mutagen = d.pop("mutagen", UNSET)

        growth_conditions = d.pop("growth_conditions", UNSET)

        outcrossed = d.pop("outcrossed", UNSET)

        made_by = d.pop("made_by", UNSET)

        dauer_defective = d.pop("dauer_defective", UNSET)

        description = d.pop("description", UNSET)

        worm_base_request_item = cls(
            name=name,
            alternative_name=alternative_name,
            gene_id=gene_id,
            source=source,
            genotype=genotype,
            phenotype=phenotype,
            mutagen=mutagen,
            growth_conditions=growth_conditions,
            outcrossed=outcrossed,
            made_by=made_by,
            dauer_defective=dauer_defective,
            description=description,
        )

        worm_base_request_item.additional_properties = d
        return worm_base_request_item

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
