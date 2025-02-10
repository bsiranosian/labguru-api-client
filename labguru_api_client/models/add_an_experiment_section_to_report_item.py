from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddAnExperimentSectionToReportItem")


@_attrs_define
class AddAnExperimentSectionToReportItem:
    """
    Attributes:
        report_id (int): the report id Example: 1.
        section_id (str): the experiment procedure id to copy Example: 32.
    """

    report_id: int
    section_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_id = self.report_id

        section_id = self.section_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "report_id": report_id,
                "section_id": section_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        report_id = d.pop("report_id")

        section_id = d.pop("section_id")

        add_an_experiment_section_to_report_item = cls(
            report_id=report_id,
            section_id=section_id,
        )

        add_an_experiment_section_to_report_item.additional_properties = d
        return add_an_experiment_section_to_report_item

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
