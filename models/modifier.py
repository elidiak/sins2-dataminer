from dataclasses import dataclass, field
from typing import Any


@dataclass
class Modifier:
    """
    Represents a modifier parsed from an ability, buff, or research block.
    Known fields can be added explicitly; all other parsed fields are stored
    in `extra` to preserve full fidelity with the original .entity data.
    """

    type: str | None = None
    value: float | None = None
    target: str | None = None

    # Arbitrary additional fields discovered during parsing
    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        """
        Assigns a parsed key/value pair to a known field if it exists,
        otherwise stores it in `extra`. Mirrors the Java behavior.
        """
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value