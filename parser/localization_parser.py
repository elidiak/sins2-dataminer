from pathlib import Path

def parse_localization(path: Path) -> dict[str, str]:
    mapping = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            mapping[key.strip()] = value.strip()
    return mapping