from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCommentItem")


@_attrs_define
class CreateCommentItem:
    """
    Attributes:
        comment (str): The content of the comment Example: This is my comment.
        commentable_id (int): ID of the item the comment is added to Example: 216.
        commentable_type (str): Type of the item the comment is added to Example: Biocollections::Plasmid.
    """

    comment: str
    commentable_id: int
    commentable_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        commentable_id = self.commentable_id

        commentable_type = self.commentable_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "commentable_id": commentable_id,
                "commentable_type": commentable_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("comment")

        commentable_id = d.pop("commentable_id")

        commentable_type = d.pop("commentable_type")

        create_comment_item = cls(
            comment=comment,
            commentable_id=commentable_id,
            commentable_type=commentable_type,
        )

        create_comment_item.additional_properties = d
        return create_comment_item

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
