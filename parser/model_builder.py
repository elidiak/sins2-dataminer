from typing import Any, Callable, Dict

from ..models.entity import Entity
from ..models.ability import Ability
from ..models.buff import Buff
from ..models.research import Research
from ..models.faction import Faction
from ..models.modifier import Modifier
from ..models.effect import Effect
from ..models.cost import Cost
from ..models.requirement import Requirement
from ..models.prerequisite import Prerequisite
from ..models.stat import Stat
from ..models.entity_reference import EntityReference

BLOCK_TYPES: Dict[str, Callable[[], Any]] = {
    "ability": Ability,
    "buff": Buff,
    "research": Research,
    "faction": Faction,
    "modifier": Modifier,
    "effect": Effect,
    "cost": Cost,
    "requirement": Requirement,
    "prerequisite": Prerequisite,
    "stat": Stat,
    "entityRef": EntityReference,
}

def build_entity(struct: dict[str, Any], name: str) -> Entity:
    entity = Entity(name=name)

    for key, value in struct.items():
        if key in BLOCK_TYPES:
            if isinstance(value, dict):
                obj = build_block(key, value)
                getattr(entity, key + "s").append(obj)
            elif isinstance(value, list):
                for item in value:
                    obj = build_block(key, item)
                    getattr(entity, key + "s").append(obj)
        else:
            entity.set_field(key, value)

    return entity

def build_block(block_type: str, struct: dict[str, Any]) -> Any:
    cls = BLOCK_TYPES[block_type]
    obj = cls()

    for key, value in struct.items():
        if key in BLOCK_TYPES:
            if isinstance(value, dict):
                nested = build_block(key, value)
                obj.extra.setdefault(key, []).append(nested)
            elif isinstance(value, list):
                for item in value:
                    nested = build_block(key, item)
                    obj.extra.setdefault(key, []).append(nested)
        else:
            obj.set_field(key, value)

    return obj