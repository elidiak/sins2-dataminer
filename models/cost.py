from dataclasses import dataclass, field
from typing import Any

@dataclass
class Cost:
    """
    Represents a cost block (credits, metal, crystal, etc.)
    """
    credits: float | None = None
    metal: float | None = None
    crystal: float | None = None
    time: float | None = None

    extra: dict[str, Any] = field(default_factory=dict)

    def set_field(self, key: str, value: Any):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extra[key] = value