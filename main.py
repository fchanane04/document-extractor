'''
Command: python3 main.py --file <file.ext> --provider <llm>
'''

import argparse
from pathlib import Path

def detect_file_ext(file_path: str) -> str:
    suffix = Path(file_path).suffix.lower()
    if not suffix:
        print("file has no extention, not supported")
    else:
        print(f"extention is {suffix}")

def main():
    parser = argparse.ArgumentParser(description="Document Extractor")
    parser.add_argument("--file", required=True, help="Path to the file")
    args = parser.parse_args()

    print(detect_file_ext(args.file))

if __name__ == "__main__":
    main()