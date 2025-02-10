from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_v1_flags_response_200_flag import PostApiV1FlagsResponse200Flag


T = TypeVar("T", bound="PostApiV1FlagsResponse200")


@_attrs_define
class PostApiV1FlagsResponse200:
    """
    Attributes:
        flag (Union[Unset, PostApiV1FlagsResponse200Flag]):
        state (Union[Unset, str]):
    """

    flag: Union[Unset, "PostApiV1FlagsResponse200Flag"] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.flag, Unset):
            flag = self.flag.to_dict()

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flag is not UNSET:
            field_dict["flag"] = flag
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_api_v1_flags_response_200_flag import PostApiV1FlagsResponse200Flag

        d = src_dict.copy()
        _flag = d.pop("flag", UNSET)
        flag: Union[Unset, PostApiV1FlagsResponse200Flag]
        if isinstance(_flag, Unset):
            flag = UNSET
        else:
            flag = PostApiV1FlagsResponse200Flag.from_dict(_flag)

        state = d.pop("state", UNSET)

        post_api_v1_flags_response_200 = cls(
            flag=flag,
            state=state,
        )

        post_api_v1_flags_response_200.additional_properties = d
        return post_api_v1_flags_response_200

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
