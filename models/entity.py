from dataclasses import dataclass, field
from typing import Any

@dataclass
class Entity:

    # Basic fields

    name: str
    abilities: list[Any] = field(default_factory=list)
    buffs: list[Any] = field(default_factory=list)
    raw: list[str] = field(default_factory=list)
    research: list[Any] = field(default_factory=list)