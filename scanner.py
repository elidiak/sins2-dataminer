from pathlib import Path
from typing import Any

from .parser.entity_parser import parse_entity
from .parser.localization_parser import parse_localization


def scan_install_dir(steamdir: Path) -> dict[str, Any]:
    """
    Python equivalent of DataMiner.java.
    Scans the Sins2 install directory, parses all .entity and .str files,
    and returns a structured dictionary ready for JSON output.
    """

    entities = []
    localization = {}

    # Parse all .entity files
    for path in steamdir.rglob("*.entity"):
        try:
            entity = parse_entity(path)
            entities.append(entity)
        except Exception as e:
            print(f"Error parsing entity file {path}: {e}")

    # Parse all localization (.str) files
    for path in steamdir.rglob("*.str"):
        try:
            loc = parse_localization(path)
            localization.update(loc)
        except Exception as e:
            print(f"Error parsing localization file {path}: {e}")

    return {
        "entities": entities,
        "localization": localization,
    }