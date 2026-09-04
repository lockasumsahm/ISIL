from dataclasses import dataclass


@dataclass(frozen=True)
class APIError:
    code: str
    message: str
    retryable: bool = False
