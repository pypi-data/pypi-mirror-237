# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ...types import Card
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPageCursor, AsyncPageCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.resource_refs import paginated_model_second_ref_list_params

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["PaginatedModelSecondRef", "AsyncPaginatedModelSecondRef"]


class PaginatedModelSecondRef(SyncAPIResource):
    with_raw_response: PaginatedModelSecondRefWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.with_raw_response = PaginatedModelSecondRefWithRawResponse(self)

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
    ) -> SyncPageCursor[Card]:
        """
        used to test a paginated method whose items type is defined in a separate
        resource in the config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/resource_refs/paginated_model_separate_resource",
            page=SyncPageCursor[Card],
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
                    paginated_model_second_ref_list_params.PaginatedModelSecondRefListParams,
                ),
            ),
            model=Card,
        )


class AsyncPaginatedModelSecondRef(AsyncAPIResource):
    with_raw_response: AsyncPaginatedModelSecondRefWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncPaginatedModelSecondRefWithRawResponse(self)

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
    ) -> AsyncPaginator[Card, AsyncPageCursor[Card]]:
        """
        used to test a paginated method whose items type is defined in a separate
        resource in the config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/resource_refs/paginated_model_separate_resource",
            page=AsyncPageCursor[Card],
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
                    paginated_model_second_ref_list_params.PaginatedModelSecondRefListParams,
                ),
            ),
            model=Card,
        )


class PaginatedModelSecondRefWithRawResponse:
    def __init__(self, paginated_model_second_ref: PaginatedModelSecondRef) -> None:
        self.list = to_raw_response_wrapper(
            paginated_model_second_ref.list,
        )


class AsyncPaginatedModelSecondRefWithRawResponse:
    def __init__(self, paginated_model_second_ref: AsyncPaginatedModelSecondRef) -> None:
        self.list = async_to_raw_response_wrapper(
            paginated_model_second_ref.list,
        )
