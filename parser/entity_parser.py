from pathlib import Path
from ..models.entity import Entity

def parse_entity(path: Path) -> Entity:
    lines = path.read_text(encoding="utf-8").splitlines()

    # TODO: implement actual parsing logic
    return Entity(name=path.stem, raw=lines)