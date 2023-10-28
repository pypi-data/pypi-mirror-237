# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ...types import MyModel
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPageOffset, AsyncPageOffset
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pagination_tests import offset_list_params

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["Offset", "AsyncOffset"]


class Offset(SyncAPIResource):
    with_raw_response: OffsetWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.with_raw_response = OffsetWithRawResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageOffset[MyModel]:
        """
        Test case for offset pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/offset",
            page=SyncPageOffset[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    offset_list_params.OffsetListParams,
                ),
            ),
            model=MyModel,
        )


class AsyncOffset(AsyncAPIResource):
    with_raw_response: AsyncOffsetWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncOffsetWithRawResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyModel, AsyncPageOffset[MyModel]]:
        """
        Test case for offset pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/offset",
            page=AsyncPageOffset[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    offset_list_params.OffsetListParams,
                ),
            ),
            model=MyModel,
        )


class OffsetWithRawResponse:
    def __init__(self, offset: Offset) -> None:
        self.list = to_raw_response_wrapper(
            offset.list,
        )


class AsyncOffsetWithRawResponse:
    def __init__(self, offset: AsyncOffset) -> None:
        self.list = async_to_raw_response_wrapper(
            offset.list,
        )
