from dataclasses import dataclass, field
from typing import Any

@dataclass
class Faction:
    """
    Represents a faction parsed from Sins2 data.
    Known fields can be added explicitly; all other
    parsed fields are stored in `extra`.
    """
    name: str | None = None
    display_name: str | None = None
    description: str | None = None

    # Lists of related objects (abilities, research, etc.)
    abilities: list[Any] = field(default_factory=list)
    buffs: list[Any] = field(default_factory=list)
    research: list[Any] = field(default_factory=list)

    # Arbitrary additional fields discovered during parsing
    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        """
        Assigns a parsed key/value pair to a known field if it exists,
        otherwise stores it in `extra`.
        """
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value