# This file was auto-generated by Fern from our API Definition.

import typing

from vellum.core.pydantic_utilities import UniversalBaseModel

from .generate_result import GenerateResult


class GenerateResponse(UniversalBaseModel):
    results: typing.List[GenerateResult]

    @property
    def texts(self) -> typing.List[str]:
        return [
            completion.text
            for result in self.results
            for completion in (result.data.completions if result.data else [])
        ]

    @property
    def text(self) -> str:
        if len(self.texts) != 1:
            raise ValueError(f"Expected exactly one completion, but got {len(self.texts)}")
        return self.texts[0]
