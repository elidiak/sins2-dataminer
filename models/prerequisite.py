from dataclasses import dataclass, field
from typing import Any

@dataclass
class Prerequisite:
    """
    Represents a prerequisite for research or faction unlocks.
    """
    name: str | None = None
    level: int | None = None

    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value