# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

from .model_string import ModelString

__all__ = ["UnionParamUnionEnumNewTypeParams"]


class UnionParamUnionEnumNewTypeParams(TypedDict, total=False):
    model: Union[ModelString, Literal["gpt-4", "gpt-3"]]
