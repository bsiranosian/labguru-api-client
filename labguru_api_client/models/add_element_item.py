from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddElementItem")


@_attrs_define
class AddElementItem:
    """Valid element types are:

    - samples
    - equipment
    - code
    - compound
    - reaction
    - text
    - steps
    - excel
    - plate


        Attributes:
            container_id (int): The ID of the section to which the element will be added
            container_type (str): The type of container in which the element will be placed Example: ExperimentProcedure.
            element_type (str): The type of element to be added
            data (Union[None, str]):
            name (Union[Unset, str]): Specifies the name of the element. If not provided, the element will be assigned a
                default name
    """

    container_id: int
    container_type: str
    element_type: str
    data: Union[None, str]
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_id = self.container_id

        container_type = self.container_type

        element_type = self.element_type

        data: Union[None, str]
        data = self.data

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container_id": container_id,
                "container_type": container_type,
                "element_type": element_type,
                "data": data,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        container_id = d.pop("container_id")

        container_type = d.pop("container_type")

        element_type = d.pop("element_type")

        def _parse_data(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        data = _parse_data(d.pop("data"))

        name = d.pop("name", UNSET)

        add_element_item = cls(
            container_id=container_id,
            container_type=container_type,
            element_type=element_type,
            data=data,
            name=name,
        )

        add_element_item.additional_properties = d
        return add_element_item

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
