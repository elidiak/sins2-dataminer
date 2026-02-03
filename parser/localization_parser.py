from pathlib import Path


def parse_localization(path: Path) -> dict[str, str]:
    """
    Python rewrite of LocalizationParser.java.
    Parses a .str localization file into a dictionary of key/value pairs.

    Behavior mirrors the Java version:
    - UTF-8 decoding
    - Skips empty lines and comment lines
    - Splits on the first '=' only
    - Trims whitespace around keys and values
    - Allows duplicate keys (later values overwrite earlier ones)
    - Ignores malformed lines gracefully
    """

    mapping: dict[str, str] = {}

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        print(f"Error reading localization file {path}: {e}")
        return mapping

    for line in lines:
        stripped = line.strip()

        # Skip empty or comment lines
        if not stripped or stripped.startswith("//") or stripped.startswith("#"):
            continue

        # Must contain '=' to be valid
        if "=" not in stripped:
            # Java version logs but continues; we mimic that
            print(f"Warning: malformed localization line in {path}: {line}")
            continue

        # Split on the FIRST '=' only
        key, value = stripped.split("=", 1)

        key = key.strip()
        value = value.strip()

        # Remove surrounding quotes if present
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]

        mapping[key] = value

    return mapping