from dataclasses import dataclass, field
from typing import Any

@dataclass
class Entity:
    """
    Represents a parsed .entity file from Sins2.
    This is the root model that aggregates abilities,
    buffs, research items, factions, and any additional
    fields discovered during parsing.
    """

    # Basic identity
    name: str | None = None
    type: str | None = None
    description: str | None = None

    # Collections of sub‑objects
    abilities: list[Any] = field(default_factory=list)
    buffs: list[Any] = field(default_factory=list)
    research: list[Any] = field(default_factory=list)
    factions: list[Any] = field(default_factory=list)
    modifiers: list[Any] = field(default_factory=list)

    # Raw file contents (for debugging or fallback parsing)
    raw: list[str] = field(default_factory=list)

    # Arbitrary additional fields discovered during parsing
    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        """
        Assigns a parsed key/value pair to a known field if it exists,
        otherwise stores it in `extra`. This mirrors the Java behavior
        where unknown fields are preserved rather than discarded.
        """
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value
