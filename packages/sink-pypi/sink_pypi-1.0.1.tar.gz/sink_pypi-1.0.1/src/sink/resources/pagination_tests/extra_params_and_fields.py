# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ...types import MyModel
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import (
    SyncGenericPageWithExtraParamsAndFields,
    AsyncGenericPageWithExtraParamsAndFields,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pagination_tests import extra_params_and_field_list_params

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["ExtraParamsAndFields", "AsyncExtraParamsAndFields"]


class ExtraParamsAndFields(SyncAPIResource):
    with_raw_response: ExtraParamsAndFieldsWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.with_raw_response = ExtraParamsAndFieldsWithRawResponse(self)

    def list(
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
    ) -> SyncGenericPageWithExtraParamsAndFields[MyModel]:
        """
        Test case for generic page types using cursor based pagination, with more params

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._get_api_list(
            "/paginated/more_params",
            page=SyncGenericPageWithExtraParamsAndFields[MyModel],
            body=maybe_transform({"foo": foo}, extra_params_and_field_list_params.ExtraParamsAndFieldListParams),
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
                    extra_params_and_field_list_params.ExtraParamsAndFieldListParams,
                ),
            ),
            model=MyModel,
            method="post",
        )


class AsyncExtraParamsAndFields(AsyncAPIResource):
    with_raw_response: AsyncExtraParamsAndFieldsWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncExtraParamsAndFieldsWithRawResponse(self)

    def list(
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
    ) -> AsyncPaginator[MyModel, AsyncGenericPageWithExtraParamsAndFields[MyModel]]:
        """
        Test case for generic page types using cursor based pagination, with more params

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._get_api_list(
            "/paginated/more_params",
            page=AsyncGenericPageWithExtraParamsAndFields[MyModel],
            body=maybe_transform({"foo": foo}, extra_params_and_field_list_params.ExtraParamsAndFieldListParams),
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
                    extra_params_and_field_list_params.ExtraParamsAndFieldListParams,
                ),
            ),
            model=MyModel,
            method="post",
        )


class ExtraParamsAndFieldsWithRawResponse:
    def __init__(self, extra_params_and_fields: ExtraParamsAndFields) -> None:
        self.list = to_raw_response_wrapper(
            extra_params_and_fields.list,
        )


class AsyncExtraParamsAndFieldsWithRawResponse:
    def __init__(self, extra_params_and_fields: AsyncExtraParamsAndFields) -> None:
        self.list = async_to_raw_response_wrapper(
            extra_params_and_fields.list,
        )
