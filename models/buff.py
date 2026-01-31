from dataclasses import dataclass, field
from typing import Any

@dataclass
class Buff:
    """
    Represents a buff parsed from a .entity file.
    Known fields can be added as attributes; everything else
    is stored in `extra` to preserve all parsed data.
    """
    name: str | None = None
    duration: float | None = None
    description: str | None = None

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