from pathlib import Path
from .cli import parse_args
from .scanner import scan_install_dir
from .writers.json_writer import write_json

def main():
    # Parse command-line arguments
    args = parse_args()

    steamdir = Path(args.steamdir)
    outdir = Path(args.output)
    
    # If the directories do not exist, raise an error
    if not steamdir.exists():
        raise FileNotFoundError(f"Steam directory '{steamdir}' does not exist.")
    
    data = scan_install_dir(steamdir)

    write_json(data, outdir)

if __name__ == "__main__":
    main()