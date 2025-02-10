from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_v1_measurements_body_item import PostApiV1MeasurementsBodyItem


T = TypeVar("T", bound="PostApiV1MeasurementsBody")


@_attrs_define
class PostApiV1MeasurementsBody:
    """
    Attributes:
        token (str):  Example: YOUR TOKEN IS HERE.
        input_name (Union[Unset, str]): The name of the form input field where the value should be positioned
        experiment_id (Union[Unset, int]): The ID of the experiment
        item (Union[Unset, PostApiV1MeasurementsBodyItem]):
    """

    token: str
    input_name: Union[Unset, str] = UNSET
    experiment_id: Union[Unset, int] = UNSET
    item: Union[Unset, "PostApiV1MeasurementsBodyItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        input_name = self.input_name

        experiment_id = self.experiment_id

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
        if input_name is not UNSET:
            field_dict["input_name"] = input_name
        if experiment_id is not UNSET:
            field_dict["experiment_id"] = experiment_id
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_api_v1_measurements_body_item import PostApiV1MeasurementsBodyItem

        d = src_dict.copy()
        token = d.pop("token")

        input_name = d.pop("input_name", UNSET)

        experiment_id = d.pop("experiment_id", UNSET)

        _item = d.pop("item", UNSET)
        item: Union[Unset, PostApiV1MeasurementsBodyItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = PostApiV1MeasurementsBodyItem.from_dict(_item)

        post_api_v1_measurements_body = cls(
            token=token,
            input_name=input_name,
            experiment_id=experiment_id,
            item=item,
        )

        post_api_v1_measurements_body.additional_properties = d
        return post_api_v1_measurements_body

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
