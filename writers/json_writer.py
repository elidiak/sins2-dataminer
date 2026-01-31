import json
from pathlib import Path

def write_json(data, output_dir: str):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    with open(out / "data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)