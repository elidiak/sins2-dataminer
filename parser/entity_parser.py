# Import Pathlib and data classes
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any

from ..models.entity import Entity
from ..models.ability import Ability
from ..models.buff import Buff


def parse_entity(path: Path) -> Entity:
    # Parse an entity file and return an Entity object.
    lines = path.read_text(encoding="utf-8").splitlines()

    # Create and return the Entity object
    entity = Entity(
        name=path.stem,
        abilities=[],
        buffs=[],
        raw=lines,
    )

    current_section = None
    buffer = {}

    for line in lines:
        stripped = line.strip()

        # Skip empty or comment lines

        if not stripped or stripped.startswith("//"):
            continue

       # Section start

        if stripped.endswith("{"):
            current_section = stripped[:-1].strip()
            buffer = {}
            continue

        # Section end

        if stripped == "}":
            if current_section == "ability":
                    ability = Ability()
                    for k, v in buffer.items():
                        ability.set_field(k, v)
                    entity.abilities.append(ability)
            elif current_section == "buff":
                entity.buffs.append(Buff(**buffer))
            current_section = None
            buffer = {}
            continue

        # Key/value inside a section

        if current_section and "=" in stripped:
            key, value = stripped.split("=", 1)
            buffer[key.strip()] = parse_value(value.strip())

    return Entity(name=path.stem, raw=lines)

def parse_value(value: str) -> Any:
    
    # Try to convert numbers
    
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value.strip('"')
