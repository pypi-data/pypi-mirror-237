# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PaginatedModelSecondRefListParams"]


class PaginatedModelSecondRefListParams(TypedDict, total=False):
    cursor: str

    limit: int
