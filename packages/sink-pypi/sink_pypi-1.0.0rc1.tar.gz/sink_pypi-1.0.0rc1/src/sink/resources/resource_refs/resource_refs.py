# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .parent import (
    Parent,
    AsyncParent,
    ParentWithRawResponse,
    AsyncParentWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .paginated_model_first_ref import (
    PaginatedModelFirstRef,
    AsyncPaginatedModelFirstRef,
    PaginatedModelFirstRefWithRawResponse,
    AsyncPaginatedModelFirstRefWithRawResponse,
)
from .paginated_model_second_ref import (
    PaginatedModelSecondRef,
    AsyncPaginatedModelSecondRef,
    PaginatedModelSecondRefWithRawResponse,
    AsyncPaginatedModelSecondRefWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Sink, AsyncSink

__all__ = ["ResourceRefs", "AsyncResourceRefs"]


class ResourceRefs(SyncAPIResource):
    paginated_model_first_ref: PaginatedModelFirstRef
    paginated_model_second_ref: PaginatedModelSecondRef
    parent: Parent
    with_raw_response: ResourceRefsWithRawResponse

    def __init__(self, client: Sink) -> None:
        super().__init__(client)
        self.paginated_model_first_ref = PaginatedModelFirstRef(client)
        self.paginated_model_second_ref = PaginatedModelSecondRef(client)
        self.parent = Parent(client)
        self.with_raw_response = ResourceRefsWithRawResponse(self)


class AsyncResourceRefs(AsyncAPIResource):
    paginated_model_first_ref: AsyncPaginatedModelFirstRef
    paginated_model_second_ref: AsyncPaginatedModelSecondRef
    parent: AsyncParent
    with_raw_response: AsyncResourceRefsWithRawResponse

    def __init__(self, client: AsyncSink) -> None:
        super().__init__(client)
        self.paginated_model_first_ref = AsyncPaginatedModelFirstRef(client)
        self.paginated_model_second_ref = AsyncPaginatedModelSecondRef(client)
        self.parent = AsyncParent(client)
        self.with_raw_response = AsyncResourceRefsWithRawResponse(self)


class ResourceRefsWithRawResponse:
    def __init__(self, resource_refs: ResourceRefs) -> None:
        self.paginated_model_first_ref = PaginatedModelFirstRefWithRawResponse(resource_refs.paginated_model_first_ref)
        self.paginated_model_second_ref = PaginatedModelSecondRefWithRawResponse(
            resource_refs.paginated_model_second_ref
        )
        self.parent = ParentWithRawResponse(resource_refs.parent)


class AsyncResourceRefsWithRawResponse:
    def __init__(self, resource_refs: AsyncResourceRefs) -> None:
        self.paginated_model_first_ref = AsyncPaginatedModelFirstRefWithRawResponse(
            resource_refs.paginated_model_first_ref
        )
        self.paginated_model_second_ref = AsyncPaginatedModelSecondRefWithRawResponse(
            resource_refs.paginated_model_second_ref
        )
        self.parent = AsyncParentWithRawResponse(resource_refs.parent)
