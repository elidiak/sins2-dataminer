from .cli import parse_args
from .scanner import scan_install_dir
from .writers.json_writer import write_json

def main():
    args = parse_args()

    data = scan_install_dir(args.steamdir)

    write_json(data, args.output)

if __name__ == "__main__":
    main()