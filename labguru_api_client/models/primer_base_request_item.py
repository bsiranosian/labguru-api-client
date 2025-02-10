from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrimerBaseRequestItem")


@_attrs_define
class PrimerBaseRequestItem:
    """
    Attributes:
        title (Union[Unset, str]): The name of the primer
        alternative_name (Union[Unset, str]): Any alternative name by which the primer may be known
        owner_id (Union[Unset, int]): id of the owner - if omitted, will default to your member id Example: Your member
            id.
        sequence (Union[Unset, str]): The nucleotide sequence of the primer
        tag (Union[Unset, str]): A unique label or tag associated with the primer
        gene_id (Union[None, Unset, int]): A reference ID linking the primer to a specific gene in your lab
        tm (Union[Unset, str]): The melting temperature (Tm) of the primer Example: 3.
        orientation (Union[None, Unset, str]): Indicates the orientation of the primer. Set "1" for forward and "0" for
            reverse. This field is optional and can be left null if orientation is not applicable Example: 1.
        target_position (Union[Unset, str]): The specific binding position of the primer on the target DNA
        fragment_size (Union[Unset, str]): The size of the DNA fragment that the primer is designed to amplify
        organism (Union[Unset, str]): The specific organism for which the primer is designed, such as "Mouse"
        used_for (Union[Unset, str]): The specific applications for which the primer is used (pcr / RT / SDM / etc.)
        restriction_site (Union[Unset, str]): Information about any restriction enzyme recognition sites incorporated
            into the primer design
        source (Union[Unset, str]): The origin or source from which the primer was obtained
        description (Union[Unset, str]): A detailed description of the primer
    """

    title: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    sequence: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    gene_id: Union[None, Unset, int] = UNSET
    tm: Union[Unset, str] = UNSET
    orientation: Union[None, Unset, str] = UNSET
    target_position: Union[Unset, str] = UNSET
    fragment_size: Union[Unset, str] = UNSET
    organism: Union[Unset, str] = UNSET
    used_for: Union[Unset, str] = UNSET
    restriction_site: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        alternative_name = self.alternative_name

        owner_id = self.owner_id

        sequence = self.sequence

        tag = self.tag

        gene_id: Union[None, Unset, int]
        if isinstance(self.gene_id, Unset):
            gene_id = UNSET
        else:
            gene_id = self.gene_id

        tm = self.tm

        orientation: Union[None, Unset, str]
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        target_position = self.target_position

        fragment_size = self.fragment_size

        organism = self.organism

        used_for = self.used_for

        restriction_site = self.restriction_site

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if tag is not UNSET:
            field_dict["tag"] = tag
        if gene_id is not UNSET:
            field_dict["gene_id"] = gene_id
        if tm is not UNSET:
            field_dict["tm"] = tm
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if target_position is not UNSET:
            field_dict["target_position"] = target_position
        if fragment_size is not UNSET:
            field_dict["fragment_size"] = fragment_size
        if organism is not UNSET:
            field_dict["organism"] = organism
        if used_for is not UNSET:
            field_dict["used_for"] = used_for
        if restriction_site is not UNSET:
            field_dict["restriction_site"] = restriction_site
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

        owner_id = d.pop("owner_id", UNSET)

        sequence = d.pop("sequence", UNSET)

        tag = d.pop("tag", UNSET)

        def _parse_gene_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        gene_id = _parse_gene_id(d.pop("gene_id", UNSET))

        tm = d.pop("tm", UNSET)

        def _parse_orientation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        target_position = d.pop("target_position", UNSET)

        fragment_size = d.pop("fragment_size", UNSET)

        organism = d.pop("organism", UNSET)

        used_for = d.pop("used_for", UNSET)

        restriction_site = d.pop("restriction_site", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        primer_base_request_item = cls(
            title=title,
            alternative_name=alternative_name,
            owner_id=owner_id,
            sequence=sequence,
            tag=tag,
            gene_id=gene_id,
            tm=tm,
            orientation=orientation,
            target_position=target_position,
            fragment_size=fragment_size,
            organism=organism,
            used_for=used_for,
            restriction_site=restriction_site,
            source=source,
            description=description,
        )

        primer_base_request_item.additional_properties = d
        return primer_base_request_item

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
