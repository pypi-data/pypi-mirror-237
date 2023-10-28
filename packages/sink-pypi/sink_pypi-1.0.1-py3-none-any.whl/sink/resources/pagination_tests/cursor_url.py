# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ...types import MyModel
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPageCursorURL, AsyncPageCursorURL
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pagination_tests import cursor_url_list_params

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["CursorURL", "AsyncCursorURL"]


class CursorURL(SyncAPIResource):
    with_raw_response: CursorURLWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.with_raw_response = CursorURLWithRawResponse(self)

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageCursorURL[MyModel]:
        """
        Test case for cursor_url pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor_url",
            page=SyncPageCursorURL[MyModel],
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
                    cursor_url_list_params.CursorURLListParams,
                ),
            ),
            model=MyModel,
        )


class AsyncCursorURL(AsyncAPIResource):
    with_raw_response: AsyncCursorURLWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCursorURLWithRawResponse(self)

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyModel, AsyncPageCursorURL[MyModel]]:
        """
        Test case for cursor_url pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor_url",
            page=AsyncPageCursorURL[MyModel],
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
                    cursor_url_list_params.CursorURLListParams,
                ),
            ),
            model=MyModel,
        )


class CursorURLWithRawResponse:
    def __init__(self, cursor_url: CursorURL) -> None:
        self.list = to_raw_response_wrapper(
            cursor_url.list,
        )


class AsyncCursorURLWithRawResponse:
    def __init__(self, cursor_url: AsyncCursorURL) -> None:
        self.list = async_to_raw_response_wrapper(
            cursor_url.list,
        )
