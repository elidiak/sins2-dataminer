from pathlib import Path
from .parser.entity_parser import parse_entity
from .parser.localization_parser import parse_localization

def scan_install_dir(steamdir: str):
    root = Path(steamdir)

    entities = []
    localizations = {}

    for path in root.rglob("*.entity"):
        entities.append(parse_entity(path))

    for path in root.rglob("*.str"):
        localizations.update(parse_localization(path))

    return {
        "entities": entities,
        "localization": localizations,
    }