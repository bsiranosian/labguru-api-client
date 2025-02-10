from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateAttachment")


@_attrs_define
class CreateAttachment:
    """
    Attributes:
        token (str):
        itemattachment (File): The file that will be uploaded.
        itemtitle (str): The title of the attachment. **This should match the file name exactly, including the file
            extension (.xlsx, .csv, etc.)**.
             Example: Project_report.pdf.
        itemattach_to_uuid (Union[Unset, str]): The UUID of the object to which the attachment will be linked.

            If this parameter is not provided, the uploaded file will be stored but not associated with any specific entity
            (unattached file).
        itemdescription (Union[Unset, str]): A brief description of the attachment content. Example: Detailed project
            report.
    """

    token: str
    itemattachment: File
    itemtitle: str
    itemattach_to_uuid: Union[Unset, str] = UNSET
    itemdescription: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        itemattachment = self.itemattachment.to_tuple()

        itemtitle = self.itemtitle

        itemattach_to_uuid = self.itemattach_to_uuid

        itemdescription = self.itemdescription

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "item[attachment]": itemattachment,
                "item[title]": itemtitle,
            }
        )
        if itemattach_to_uuid is not UNSET:
            field_dict["item[attach_to_uuid]"] = itemattach_to_uuid
        if itemdescription is not UNSET:
            field_dict["item[description]"] = itemdescription

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        token = (None, str(self.token).encode(), "text/plain")

        itemattachment = self.itemattachment.to_tuple()

        itemtitle = (None, str(self.itemtitle).encode(), "text/plain")

        itemattach_to_uuid = (
            self.itemattach_to_uuid
            if isinstance(self.itemattach_to_uuid, Unset)
            else (None, str(self.itemattach_to_uuid).encode(), "text/plain")
        )

        itemdescription = (
            self.itemdescription
            if isinstance(self.itemdescription, Unset)
            else (None, str(self.itemdescription).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "token": token,
                "item[attachment]": itemattachment,
                "item[title]": itemtitle,
            }
        )
        if itemattach_to_uuid is not UNSET:
            field_dict["item[attach_to_uuid]"] = itemattach_to_uuid
        if itemdescription is not UNSET:
            field_dict["item[description]"] = itemdescription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        itemattachment = File(payload=BytesIO(d.pop("item[attachment]")))

        itemtitle = d.pop("item[title]")

        itemattach_to_uuid = d.pop("item[attach_to_uuid]", UNSET)

        itemdescription = d.pop("item[description]", UNSET)

        create_attachment = cls(
            token=token,
            itemattachment=itemattachment,
            itemtitle=itemtitle,
            itemattach_to_uuid=itemattach_to_uuid,
            itemdescription=itemdescription,
        )

        create_attachment.additional_properties = d
        return create_attachment

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
