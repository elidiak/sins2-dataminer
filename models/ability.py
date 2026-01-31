from dataclasses import dataclass, field
from typing import Any

@dataclass
class Ability:
    
    """
    Represents an ability parsed from a .entity file.
    Fields are dynamically populated from the parser.
    """

    name: str | None = None
    cooldown: float | None = None
    description: str | None = None

    # Catch-all for any additional fields the parser discovers

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