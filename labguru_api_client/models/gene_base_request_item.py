from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneBaseRequestItem")


@_attrs_define
class GeneBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): The name of the gene
        alternative_name (Union[Unset, str]): Alternative gene name.
        expression_location (Union[Unset, str]): Location of gene expression.
        pathway (Union[Unset, str]): Involved metabolic pathway.
        sequence (Union[Unset, str]): Gene sequence. Example: ACTGACGACATGGTTCTGACCTGA.
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        source (Union[Unset, str]): The origin or source from which the gene was obtained.
        description (Union[Unset, str]): Detailed gene information.
    """

    title: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    expression_location: Union[Unset, str] = UNSET
    pathway: Union[Unset, str] = UNSET
    sequence: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        alternative_name = self.alternative_name

        expression_location = self.expression_location

        pathway = self.pathway

        sequence = self.sequence

        owner_id = self.owner_id

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if expression_location is not UNSET:
            field_dict["expression_location"] = expression_location
        if pathway is not UNSET:
            field_dict["pathway"] = pathway
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        expression_location = d.pop("expression_location", UNSET)

        pathway = d.pop("pathway", UNSET)

        sequence = d.pop("sequence", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        gene_base_request_item = cls(
            title=title,
            alternative_name=alternative_name,
            expression_location=expression_location,
            pathway=pathway,
            sequence=sequence,
            owner_id=owner_id,
            source=source,
            description=description,
        )

        gene_base_request_item.additional_properties = d
        return gene_base_request_item

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
