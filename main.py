"""
markdown-to-html
A utility that converts Markdown files to HTML
"""

import argparse
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A utility that converts Markdown files to HTML")
    parser.add_argument("--version", action="version", version="0.1.0")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("Project: markdown-to-html")
    print("Status: ready")
    return 0


if __name__ == "__main__":
    sys.exit(main())