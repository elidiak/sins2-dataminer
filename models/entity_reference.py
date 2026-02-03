from dataclasses import dataclass, field
from typing import Any

@dataclass
class EntityReference:
    """
    Represents a reference to another entity (e.g., for spawns, upgrades).
    """
    id: str | None = None
    count: int | None = None

    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value