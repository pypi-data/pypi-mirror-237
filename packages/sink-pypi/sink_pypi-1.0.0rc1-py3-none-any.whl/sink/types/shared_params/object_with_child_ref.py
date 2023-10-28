# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from ...types import shared_params

__all__ = ["ObjectWithChildRef"]


class ObjectWithChildRef(TypedDict, total=False):
    bar: shared_params.SimpleObject

    foo: str
