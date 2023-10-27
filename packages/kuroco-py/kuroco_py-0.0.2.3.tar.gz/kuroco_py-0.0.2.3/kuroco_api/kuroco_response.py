from dataclasses import dataclass

@dataclass
class KurocoResponse:
    status: int
    value: dict