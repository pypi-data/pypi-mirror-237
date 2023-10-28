# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .cursor import (
    Cursor,
    AsyncCursor,
    CursorWithRawResponse,
    AsyncCursorWithRawResponse,
)
from .offset import (
    Offset,
    AsyncOffset,
    OffsetWithRawResponse,
    AsyncOffsetWithRawResponse,
)
from .concrete import (
    Concrete,
    AsyncConcrete,
    ConcreteWithRawResponse,
    AsyncConcreteWithRawResponse,
)
from .cursor_url import (
    CursorURL,
    AsyncCursorURL,
    CursorURLWithRawResponse,
    AsyncCursorURLWithRawResponse,
)
from .fake_pages import (
    FakePages,
    AsyncFakePages,
    FakePagesWithRawResponse,
    AsyncFakePagesWithRawResponse,
)
from .hypermedia import (
    Hypermedia,
    AsyncHypermedia,
    HypermediaWithRawResponse,
    AsyncHypermediaWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .page_number import (
    PageNumber,
    AsyncPageNumber,
    PageNumberWithRawResponse,
    AsyncPageNumberWithRawResponse,
)
from .hypermedia_raw import (
    HypermediaRaw,
    AsyncHypermediaRaw,
    HypermediaRawWithRawResponse,
    AsyncHypermediaRawWithRawResponse,
)
from .extra_params_and_fields import (
    ExtraParamsAndFields,
    AsyncExtraParamsAndFields,
    ExtraParamsAndFieldsWithRawResponse,
    AsyncExtraParamsAndFieldsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["PaginationTests", "AsyncPaginationTests"]


class PaginationTests(SyncAPIResource):
    concrete: Concrete
    page_number: PageNumber
    cursor: Cursor
    cursor_url: CursorURL
    offset: Offset
    fake_pages: FakePages
    hypermedia: Hypermedia
    extra_params_and_fields: ExtraParamsAndFields
    hypermedia_raw: HypermediaRaw
    with_raw_response: PaginationTestsWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.concrete = Concrete(client)
        self.page_number = PageNumber(client)
        self.cursor = Cursor(client)
        self.cursor_url = CursorURL(client)
        self.offset = Offset(client)
        self.fake_pages = FakePages(client)
        self.hypermedia = Hypermedia(client)
        self.extra_params_and_fields = ExtraParamsAndFields(client)
        self.hypermedia_raw = HypermediaRaw(client)
        self.with_raw_response = PaginationTestsWithRawResponse(self)


class AsyncPaginationTests(AsyncAPIResource):
    concrete: AsyncConcrete
    page_number: AsyncPageNumber
    cursor: AsyncCursor
    cursor_url: AsyncCursorURL
    offset: AsyncOffset
    fake_pages: AsyncFakePages
    hypermedia: AsyncHypermedia
    extra_params_and_fields: AsyncExtraParamsAndFields
    hypermedia_raw: AsyncHypermediaRaw
    with_raw_response: AsyncPaginationTestsWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.concrete = AsyncConcrete(client)
        self.page_number = AsyncPageNumber(client)
        self.cursor = AsyncCursor(client)
        self.cursor_url = AsyncCursorURL(client)
        self.offset = AsyncOffset(client)
        self.fake_pages = AsyncFakePages(client)
        self.hypermedia = AsyncHypermedia(client)
        self.extra_params_and_fields = AsyncExtraParamsAndFields(client)
        self.hypermedia_raw = AsyncHypermediaRaw(client)
        self.with_raw_response = AsyncPaginationTestsWithRawResponse(self)


class PaginationTestsWithRawResponse:
    def __init__(self, pagination_tests: PaginationTests) -> None:
        self.concrete = ConcreteWithRawResponse(pagination_tests.concrete)
        self.page_number = PageNumberWithRawResponse(pagination_tests.page_number)
        self.cursor = CursorWithRawResponse(pagination_tests.cursor)
        self.cursor_url = CursorURLWithRawResponse(pagination_tests.cursor_url)
        self.offset = OffsetWithRawResponse(pagination_tests.offset)
        self.fake_pages = FakePagesWithRawResponse(pagination_tests.fake_pages)
        self.hypermedia = HypermediaWithRawResponse(pagination_tests.hypermedia)
        self.extra_params_and_fields = ExtraParamsAndFieldsWithRawResponse(pagination_tests.extra_params_and_fields)
        self.hypermedia_raw = HypermediaRawWithRawResponse(pagination_tests.hypermedia_raw)


class AsyncPaginationTestsWithRawResponse:
    def __init__(self, pagination_tests: AsyncPaginationTests) -> None:
        self.concrete = AsyncConcreteWithRawResponse(pagination_tests.concrete)
        self.page_number = AsyncPageNumberWithRawResponse(pagination_tests.page_number)
        self.cursor = AsyncCursorWithRawResponse(pagination_tests.cursor)
        self.cursor_url = AsyncCursorURLWithRawResponse(pagination_tests.cursor_url)
        self.offset = AsyncOffsetWithRawResponse(pagination_tests.offset)
        self.fake_pages = AsyncFakePagesWithRawResponse(pagination_tests.fake_pages)
        self.hypermedia = AsyncHypermediaWithRawResponse(pagination_tests.hypermedia)
        self.extra_params_and_fields = AsyncExtraParamsAndFieldsWithRawResponse(
            pagination_tests.extra_params_and_fields
        )
        self.hypermedia_raw = AsyncHypermediaRawWithRawResponse(pagination_tests.hypermedia_raw)
