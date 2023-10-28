# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import (
    SyncMyConcretePage,
    AsyncMyConcretePage,
    SyncConcretePageWithExtraParamsAndFields,
    AsyncConcretePageWithExtraParamsAndFields,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pagination_tests import (
    MyConcretePageItem,
    concrete_list_params,
    concrete_list_extra_params_and_fields_params,
)

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["Concrete", "AsyncConcrete"]


class Concrete(SyncAPIResource):
    with_raw_response: ConcreteWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.with_raw_response = ConcreteWithRawResponse(self)

    def list(
        self,
        *,
        my_cursor: str,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncMyConcretePage[MyConcretePageItem]:
        """
        Test case for concrete page types using cursor based pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/concrete/cursor",
            page=SyncMyConcretePage[MyConcretePageItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "my_cursor": my_cursor,
                        "limit": limit,
                    },
                    concrete_list_params.ConcreteListParams,
                ),
            ),
            model=MyConcretePageItem,
        )

    def list_extra_params_and_fields(
        self,
        *,
        my_cursor: str,
        limit: int | NotGiven = NOT_GIVEN,
        foo: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> SyncConcretePageWithExtraParamsAndFields[MyConcretePageItem]:
        """
        Test case for concrete page types using cursor based pagination, with more
        params

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._get_api_list(
            "/paginated/concrete/more_params",
            page=SyncConcretePageWithExtraParamsAndFields[MyConcretePageItem],
            body=maybe_transform(
                {"foo": foo}, concrete_list_extra_params_and_fields_params.ConcreteListExtraParamsAndFieldsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "my_cursor": my_cursor,
                        "limit": limit,
                    },
                    concrete_list_extra_params_and_fields_params.ConcreteListExtraParamsAndFieldsParams,
                ),
            ),
            model=MyConcretePageItem,
            method="post",
        )


class AsyncConcrete(AsyncAPIResource):
    with_raw_response: AsyncConcreteWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncConcreteWithRawResponse(self)

    def list(
        self,
        *,
        my_cursor: str,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyConcretePageItem, AsyncMyConcretePage[MyConcretePageItem]]:
        """
        Test case for concrete page types using cursor based pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/concrete/cursor",
            page=AsyncMyConcretePage[MyConcretePageItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "my_cursor": my_cursor,
                        "limit": limit,
                    },
                    concrete_list_params.ConcreteListParams,
                ),
            ),
            model=MyConcretePageItem,
        )

    def list_extra_params_and_fields(
        self,
        *,
        my_cursor: str,
        limit: int | NotGiven = NOT_GIVEN,
        foo: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AsyncPaginator[MyConcretePageItem, AsyncConcretePageWithExtraParamsAndFields[MyConcretePageItem]]:
        """
        Test case for concrete page types using cursor based pagination, with more
        params

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._get_api_list(
            "/paginated/concrete/more_params",
            page=AsyncConcretePageWithExtraParamsAndFields[MyConcretePageItem],
            body=maybe_transform(
                {"foo": foo}, concrete_list_extra_params_and_fields_params.ConcreteListExtraParamsAndFieldsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "my_cursor": my_cursor,
                        "limit": limit,
                    },
                    concrete_list_extra_params_and_fields_params.ConcreteListExtraParamsAndFieldsParams,
                ),
            ),
            model=MyConcretePageItem,
            method="post",
        )


class ConcreteWithRawResponse:
    def __init__(self, concrete: Concrete) -> None:
        self.list = to_raw_response_wrapper(
            concrete.list,
        )
        self.list_extra_params_and_fields = to_raw_response_wrapper(
            concrete.list_extra_params_and_fields,
        )


class AsyncConcreteWithRawResponse:
    def __init__(self, concrete: AsyncConcrete) -> None:
        self.list = async_to_raw_response_wrapper(
            concrete.list,
        )
        self.list_extra_params_and_fields = async_to_raw_response_wrapper(
            concrete.list_extra_params_and_fields,
        )
