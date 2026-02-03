from dataclasses import dataclass, field
from typing import Any

@dataclass
class Requirement:
    """
    Represents a requirement for an ability, buff, or research item.
    """
    type: str | None = None
    value: Any = None

    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value