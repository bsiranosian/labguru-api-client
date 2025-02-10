import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaperBaseRequestItem")


@_attrs_define
class PaperBaseRequestItem:
    """
    Attributes:
        name (Union[Unset, str]): the papers title  Example: A paper title.
        journal (Union[Unset, str]): the time period in numbers Example: 15.
        authors (Union[Unset, str]):  Example: Lab user.
        publication_date (Union[Unset, datetime.date]): in the following format yyyy-mm-dd  Example: 2021-11-21.
        volume (Union[Unset, str]): volume Example: 15.
        pages (Union[Unset, str]): pages Example: 3.
        url (Union[Unset, str]): www.link.com Example: www.someUrl.com.
        doi (Union[Unset, str]): digital object identifier Example: 10.1002/aur21.
        review (Union[Unset, str]): Abstract Example: review.
    """

    name: Union[Unset, str] = UNSET
    journal: Union[Unset, str] = UNSET
    authors: Union[Unset, str] = UNSET
    publication_date: Union[Unset, datetime.date] = UNSET
    volume: Union[Unset, str] = UNSET
    pages: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    doi: Union[Unset, str] = UNSET
    review: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        journal = self.journal

        authors = self.authors

        publication_date: Union[Unset, str] = UNSET
        if not isinstance(self.publication_date, Unset):
            publication_date = self.publication_date.isoformat()

        volume = self.volume

        pages = self.pages

        url = self.url

        doi = self.doi

        review = self.review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if journal is not UNSET:
            field_dict["journal"] = journal
        if authors is not UNSET:
            field_dict["authors"] = authors
        if publication_date is not UNSET:
            field_dict["publication_date"] = publication_date
        if volume is not UNSET:
            field_dict["volume"] = volume
        if pages is not UNSET:
            field_dict["pages"] = pages
        if url is not UNSET:
            field_dict["url"] = url
        if doi is not UNSET:
            field_dict["doi"] = doi
        if review is not UNSET:
            field_dict["review"] = review

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        journal = d.pop("journal", UNSET)

        authors = d.pop("authors", UNSET)

        _publication_date = d.pop("publication_date", UNSET)
        publication_date: Union[Unset, datetime.date]
        if isinstance(_publication_date, Unset):
            publication_date = UNSET
        else:
            publication_date = isoparse(_publication_date).date()

        volume = d.pop("volume", UNSET)

        pages = d.pop("pages", UNSET)

        url = d.pop("url", UNSET)

        doi = d.pop("doi", UNSET)

        review = d.pop("review", UNSET)

        paper_base_request_item = cls(
            name=name,
            journal=journal,
            authors=authors,
            publication_date=publication_date,
            volume=volume,
            pages=pages,
            url=url,
            doi=doi,
            review=review,
        )

        paper_base_request_item.additional_properties = d
        return paper_base_request_item

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
