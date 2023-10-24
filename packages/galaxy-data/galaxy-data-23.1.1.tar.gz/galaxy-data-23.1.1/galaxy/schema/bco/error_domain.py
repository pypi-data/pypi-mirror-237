# generated by datamodel-codegen:
#   filename:  https://opensource.ieee.org/2791-object/ieee-2791-schema/-/raw/master/error_domain.json
#   timestamp: 2022-09-13T23:51:49+00:00

from __future__ import annotations

from typing import (
    Any,
    Dict,
)

from pydantic import (
    BaseModel,
    Extra,
    Field,
)


class ErrorDomain(BaseModel):
    class Config:
        extra = Extra.forbid

    empirical_error: Dict[str, Any] = Field(
        ...,
        description="empirically determined values such as limits of detectability, false positives, false negatives, statistical confidence of outcomes, etc. This can be measured by running the algorithm on multiple data samples of the usability domain or through the use of carefully designed in-silico data.",
        title="Empirical Error",
    )
    algorithmic_error: Dict[str, Any] = Field(
        ...,
        description="descriptive of errors that originate by fuzziness of the algorithms, driven by stochastic processes, in dynamically parallelized multi-threaded executions, or in machine learning methodologies where the state of the machine can affect the outcome.",
        title="Algorithmic Error",
    )
