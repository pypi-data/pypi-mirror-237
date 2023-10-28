# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .import_ import (
    ImportResource,
    AsyncImportResource,
    ImportResourceWithRawResponse,
    AsyncImportResourceWithRawResponse,
)
from .methods import (
    Methods,
    AsyncMethods,
    MethodsWithRawResponse,
    AsyncMethodsWithRawResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ...._client import Sink, AsyncSink

__all__ = ["ReservedNames", "AsyncReservedNames"]


class ReservedNames(SyncAPIResource):
    import_: ImportResource
    methods: Methods
    with_raw_response: ReservedNamesWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.import_ = ImportResource(client)
        self.methods = Methods(client)
        self.with_raw_response = ReservedNamesWithRawResponse(self)


class AsyncReservedNames(AsyncAPIResource):
    import_: AsyncImportResource
    methods: AsyncMethods
    with_raw_response: AsyncReservedNamesWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.import_ = AsyncImportResource(client)
        self.methods = AsyncMethods(client)
        self.with_raw_response = AsyncReservedNamesWithRawResponse(self)


class ReservedNamesWithRawResponse:
    def __init__(self, reserved_names: ReservedNames) -> None:
        self.import_ = ImportResourceWithRawResponse(reserved_names.import_)
        self.methods = MethodsWithRawResponse(reserved_names.methods)


class AsyncReservedNamesWithRawResponse:
    def __init__(self, reserved_names: AsyncReservedNames) -> None:
        self.import_ = AsyncImportResourceWithRawResponse(reserved_names.import_)
        self.methods = AsyncMethodsWithRawResponse(reserved_names.methods)
