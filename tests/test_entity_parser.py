from pathlib import Path
from sins2_dataminer.parser.entity_parser import parse_entity
from sins2_dataminer.models.entity import Entity

def test_full_entity_parse(tmp_path: Path):
    content = """
    name = "Frigate"
    hull = 1200

    ability {
        type = "ShieldBoost"
        amount = 50
    }
    """

    file = tmp_path / "frigate.entity"
    file.write_text(content, encoding="utf-8")

    entity = parse_entity(file)

    assert isinstance(entity, Entity)
    assert entity.name == "frigate"  # from filename
    assert entity.hull == 1200

    assert len(entity.abilities) == 1
    ability = entity.abilities[0]
    assert ability.type == "ShieldBoost"
    assert ability.amount == 50