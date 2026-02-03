from dataclasses import dataclass, field
from typing import Any

@dataclass
class Stat:
    """
    Represents a stat block inside an entity or ability.
    """
    name: str | None = None
    value: float | None = None
    unit: str | None = None

    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value