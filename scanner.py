from pathlib import Path
from typing import Any
import json

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
    for path in steamdir.rglob("entities\\*"):
        try:
            entity = parse_entity(path)
            entities.append(entity)
        except Exception as e:
            print(f"Error parsing entity file {path}: {e}")

    # Parse all localization (.str) files
    localization_path = steamdir / "localized_text" / "en.localized_text"
    try:
        with open(localization_path, encoding="utf-8") as f:
            localization = json.load(f)
    except Exception as e:
        print(f"Error parsing localization file {localization_path}: {e}")

    return {
        "entities": entities,
        "localization": localization,
    }