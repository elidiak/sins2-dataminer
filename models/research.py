from dataclasses import dataclass, field
from typing import Any

@dataclass
class Research:
    """
    Represents a research item parsed from a .entity file.
    Known fields can be added explicitly; all other fields
    are stored in `extra` to preserve full fidelity.
    """
    name: str | None = None
    tier: int | None = None
    description: str | None = None
    cost: float | None = None

    # Stores any additional fields discovered during parsing
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