# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...types.types import ArrayFloatItemsResponse, ArrayObjectItemsResponse
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["Arrays", "AsyncArrays"]


class Arrays(SyncAPIResource):
    with_raw_response: ArraysWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.with_raw_response = ArraysWithRawResponse(self)

    def float_items(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ArrayFloatItemsResponse:
        """Endpoint with a response schema that is an array of number types."""
        return self._get(
            "/types/array/float_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrayFloatItemsResponse,
        )

    def object_items(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ArrayObjectItemsResponse:
        """Endpoint with a response schema that is an array of in-line object types."""
        return self._get(
            "/types/array/object_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrayObjectItemsResponse,
        )


class AsyncArrays(AsyncAPIResource):
    with_raw_response: AsyncArraysWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncArraysWithRawResponse(self)

    async def float_items(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ArrayFloatItemsResponse:
        """Endpoint with a response schema that is an array of number types."""
        return await self._get(
            "/types/array/float_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrayFloatItemsResponse,
        )

    async def object_items(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ArrayObjectItemsResponse:
        """Endpoint with a response schema that is an array of in-line object types."""
        return await self._get(
            "/types/array/object_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrayObjectItemsResponse,
        )


class ArraysWithRawResponse:
    def __init__(self, arrays: Arrays) -> None:
        self.float_items = to_raw_response_wrapper(
            arrays.float_items,
        )
        self.object_items = to_raw_response_wrapper(
            arrays.object_items,
        )


class AsyncArraysWithRawResponse:
    def __init__(self, arrays: AsyncArrays) -> None:
        self.float_items = async_to_raw_response_wrapper(
            arrays.float_items,
        )
        self.object_items = async_to_raw_response_wrapper(
            arrays.object_items,
        )
