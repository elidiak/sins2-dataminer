import json
from pathlib import Path
from dataclasses import asdict, is_dataclass
from typing import Any


def _convert(obj: Any) -> Any:
    """
    Recursively convert dataclasses and custom objects into
    JSON‑serializable structures. This mirrors the Java behavior
    where objects are flattened into maps before writing.
    """
    if is_dataclass(obj):
        return {k: _convert(v) for k, v in asdict(obj).items()}

    if isinstance(obj, dict):
        return {k: _convert(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [_convert(v) for v in obj]

    return obj


def write_json(data: dict[str, Any], output_dir: Path):
    """
    Python equivalent of JsonWriter.java.
    Writes the aggregated data (entities, localization, etc.)
    into JSON files inside the output directory.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    # Convert dataclasses → dicts before writing
    serializable = _convert(data)

    out_file = output_dir / "data.json"

    with out_file.open("w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)