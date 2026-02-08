from ..parser.model_builder import build_entity
from ..models.ability import Ability
from ..models.entity import Entity

def test_build_entity_simple_fields():
    struct = {"hull": 1200, "name": "Frigate"}
    entity = build_entity(struct, name="Frigate")

    assert isinstance(entity, Entity)
    assert entity.hull == 1200
    assert entity.name == "Frigate"

def test_build_entity_with_ability():
    struct = {
        "ability": {
            "type": "ShieldBoost",
            "amount": 50
        }
    }

    entity = build_entity(struct, name="Test")

    assert len(entity.abilities) == 1
    ability = entity.abilities[0]

    assert isinstance(ability, Ability)
    assert ability.type == "ShieldBoost"
    assert ability.amount == 50

def test_nested_blocks_in_extra():
    struct = {
        "ability": {
            "modifier": {
                "type": "DamageIncrease",
                "value": 0.15
            }
        }
    }

    entity = build_entity(struct, name="Test")
    ability = entity.abilities[0]

    assert "modifier" in ability.extra
    assert ability.extra["modifier"][0].type == "DamageIncrease"