import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Sins2 Dataminer (Python rewrite)")
    parser.add_argument("-sd", "--steamdir", required=True, help="Path to Sins2 install directory")
    parser.add_argument("-o", "--output", required=True, help="Output directory for wiki JSON")
    return parser.parse_args()
