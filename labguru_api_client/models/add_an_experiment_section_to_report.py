from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_an_experiment_section_to_report_item import AddAnExperimentSectionToReportItem


T = TypeVar("T", bound="AddAnExperimentSectionToReport")


@_attrs_define
class AddAnExperimentSectionToReport:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        item (Union[Unset, AddAnExperimentSectionToReportItem]):
    """

    token: str
    item: Union[Unset, "AddAnExperimentSectionToReportItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.add_an_experiment_section_to_report_item import AddAnExperimentSectionToReportItem

        d = src_dict.copy()
        token = d.pop("token")

        _item = d.pop("item", UNSET)
        item: Union[Unset, AddAnExperimentSectionToReportItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = AddAnExperimentSectionToReportItem.from_dict(_item)

        add_an_experiment_section_to_report = cls(
            token=token,
            item=item,
        )

        add_an_experiment_section_to_report.additional_properties = d
        return add_an_experiment_section_to_report

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
