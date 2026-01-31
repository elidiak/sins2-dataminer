from pathlib import Path

def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()