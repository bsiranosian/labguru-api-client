from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_v1_shopping_list_add_item_response_200_item import (
        PostApiV1ShoppingListAddItemResponse200Item,
    )


T = TypeVar("T", bound="PostApiV1ShoppingListAddItemResponse200")


@_attrs_define
class PostApiV1ShoppingListAddItemResponse200:
    """
    Attributes:
        success (Union[Unset, bool]): Indicates whether the operation was successful. Example: True.
        payload (Union[Unset, str]): A message detailing the outcome of the operation. Example: Your order was
            successfully submitted..
        lineitem_id (Union[Unset, int]): The ID of the order. Example: 76.
        item (Union[Unset, PostApiV1ShoppingListAddItemResponse200Item]): Detailed information about the item, returned
            as a JSON object.
    """

    success: Union[Unset, bool] = UNSET
    payload: Union[Unset, str] = UNSET
    lineitem_id: Union[Unset, int] = UNSET
    item: Union[Unset, "PostApiV1ShoppingListAddItemResponse200Item"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        payload = self.payload

        lineitem_id = self.lineitem_id

        item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if payload is not UNSET:
            field_dict["payload"] = payload
        if lineitem_id is not UNSET:
            field_dict["lineitem_id"] = lineitem_id
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_api_v1_shopping_list_add_item_response_200_item import (
            PostApiV1ShoppingListAddItemResponse200Item,
        )

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        payload = d.pop("payload", UNSET)

        lineitem_id = d.pop("lineitem_id", UNSET)

        _item = d.pop("item", UNSET)
        item: Union[Unset, PostApiV1ShoppingListAddItemResponse200Item]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = PostApiV1ShoppingListAddItemResponse200Item.from_dict(_item)

        post_api_v1_shopping_list_add_item_response_200 = cls(
            success=success,
            payload=payload,
            lineitem_id=lineitem_id,
            item=item,
        )

        post_api_v1_shopping_list_add_item_response_200.additional_properties = d
        return post_api_v1_shopping_list_add_item_response_200

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
