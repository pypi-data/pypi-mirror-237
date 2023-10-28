# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...types import MyModel
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import (
    SyncPageCursor,
    AsyncPageCursor,
    SyncPageCursorNestedResponseProp,
    AsyncPageCursorNestedResponseProp,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pagination_tests import (
    cursor_list_params,
    cursor_list_nested_response_prop_params,
)

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["Cursor", "AsyncCursor"]


class Cursor(SyncAPIResource):
    with_raw_response: CursorWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.with_raw_response = CursorWithRawResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageCursor[MyModel]:
        """
        Test case for cursor pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor",
            page=SyncPageCursor[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    cursor_list_params.CursorListParams,
                ),
            ),
            model=MyModel,
        )

    def list_nested_response_prop(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageCursorNestedResponseProp[MyModel]:
        """
        Test case for cursor pagination that returns a cursor under a nested property.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor_nested_response_prop",
            page=SyncPageCursorNestedResponseProp[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    cursor_list_nested_response_prop_params.CursorListNestedResponsePropParams,
                ),
            ),
            model=MyModel,
        )


class AsyncCursor(AsyncAPIResource):
    with_raw_response: AsyncCursorWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCursorWithRawResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyModel, AsyncPageCursor[MyModel]]:
        """
        Test case for cursor pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor",
            page=AsyncPageCursor[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    cursor_list_params.CursorListParams,
                ),
            ),
            model=MyModel,
        )

    def list_nested_response_prop(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyModel, AsyncPageCursorNestedResponseProp[MyModel]]:
        """
        Test case for cursor pagination that returns a cursor under a nested property.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor_nested_response_prop",
            page=AsyncPageCursorNestedResponseProp[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    cursor_list_nested_response_prop_params.CursorListNestedResponsePropParams,
                ),
            ),
            model=MyModel,
        )


class CursorWithRawResponse:
    def __init__(self, cursor: Cursor) -> None:
        self.list = to_raw_response_wrapper(
            cursor.list,
        )
        self.list_nested_response_prop = to_raw_response_wrapper(
            cursor.list_nested_response_prop,
        )


class AsyncCursorWithRawResponse:
    def __init__(self, cursor: AsyncCursor) -> None:
        self.list = async_to_raw_response_wrapper(
            cursor.list,
        )
        self.list_nested_response_prop = async_to_raw_response_wrapper(
            cursor.list_nested_response_prop,
        )
