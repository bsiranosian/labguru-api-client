from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RodentSpecimenBaseRequestItem")


@_attrs_define
class RodentSpecimenBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): The name of the rodent specimen Example: rodent-21.
        status (Union[Unset, str]): the status of the rodent: alive, dead, missing, sacrificed Example: alive.
        description (Union[Unset, str]): Description of the rodent specimen Example: General description.
        alternative_name (Union[Unset, str]): additional name for the rodent specimen Example: rodent-22.
        owner_id (Union[Unset, int]): id of the owner - by default it's your member id Example: Your member id.
        genotype (Union[Unset, str]): genotype Example: PP.
        phenotype (Union[Unset, str]): phenotype Example: homozygous viable.
        ear_tag (Union[Unset, str]): ear tag Example: ET-2930.
        coat_tag (Union[Unset, str]): coat tag Example: CT-231.
        sex (Union[Unset, str]): sex of the rodent: male, femal, unknown Example: male.
        ethics (Union[Unset, str]): ethics approval id Example: 392019998.
        dob (Union[Unset, str]): Date of birth (yyyy-mm-dd) Example: 2021-02-03.
        dod (Union[Unset, str]): Date of death (yyyy-mm-dd) Example: 2022-02-03.
        source (Union[Unset, str]): source Example: ACYW.
    """

    name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    alternative_name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    genotype: Union[Unset, str] = UNSET
    phenotype: Union[Unset, str] = UNSET
    ear_tag: Union[Unset, str] = UNSET
    coat_tag: Union[Unset, str] = UNSET
    sex: Union[Unset, str] = UNSET
    ethics: Union[Unset, str] = UNSET
    dob: Union[Unset, str] = UNSET
    dod: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        description = self.description

        alternative_name = self.alternative_name

        owner_id = self.owner_id

        genotype = self.genotype

        phenotype = self.phenotype

        ear_tag = self.ear_tag

        coat_tag = self.coat_tag

        sex = self.sex

        ethics = self.ethics

        dob = self.dob

        dod = self.dod

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if phenotype is not UNSET:
            field_dict["phenotype"] = phenotype
        if ear_tag is not UNSET:
            field_dict["ear_tag"] = ear_tag
        if coat_tag is not UNSET:
            field_dict["coat_tag"] = coat_tag
        if sex is not UNSET:
            field_dict["sex"] = sex
        if ethics is not UNSET:
            field_dict["ethics"] = ethics
        if dob is not UNSET:
            field_dict["dob"] = dob
        if dod is not UNSET:
            field_dict["dod"] = dod
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        description = d.pop("description", UNSET)

        alternative_name = d.pop("alternative_name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        genotype = d.pop("genotype", UNSET)

        phenotype = d.pop("phenotype", UNSET)

        ear_tag = d.pop("ear_tag", UNSET)

        coat_tag = d.pop("coat_tag", UNSET)

        sex = d.pop("sex", UNSET)

        ethics = d.pop("ethics", UNSET)

        dob = d.pop("dob", UNSET)

        dod = d.pop("dod", UNSET)

        source = d.pop("source", UNSET)

        rodent_specimen_base_request_item = cls(
            name=name,
            status=status,
            description=description,
            alternative_name=alternative_name,
            owner_id=owner_id,
            genotype=genotype,
            phenotype=phenotype,
            ear_tag=ear_tag,
            coat_tag=coat_tag,
            sex=sex,
            ethics=ethics,
            dob=dob,
            dod=dod,
            source=source,
        )

        rodent_specimen_base_request_item.additional_properties = d
        return rodent_specimen_base_request_item

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
