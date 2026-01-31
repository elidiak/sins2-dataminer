from dataclasses import dataclass
from typing import Any

@dataclass
class Entity:
    name: str
    raw: list[str]
    # Add parsed fields as you port logic