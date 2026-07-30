"""
LithoForge

Copyright (c) 2026 Benjamin Lloyd and Contributors

Licensed under the MIT License.
See LICENSE for details.
"""

import sys
from pathlib import Path


def inspect_ctb(filename):
    """
    Read a CTB file and print basic information.
    """

    path = Path(filename)

    if not path.exists():
        print(f"Error: '{filename}' not found.")
        return

    file_size = path.stat().st_size

    print("=" * 60)
    print("LithoForge CTB Inspector")
    print("=" * 60)
    print(f"File : {path.name}")
    print(f"Path : {path}")
    print(f"Size : {file_size:,} bytes")

    with path.open("rb") as file:
        header = file.read(64)

    print("\nFirst 64 bytes:\n")

    for offset in range(0, len(header), 16):
        chunk = header[offset:offset + 16]
        hex_string = " ".join(f"{byte:02X}" for byte in chunk)
        print(f"{offset:04X}: {hex_string}")

    print()


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("    python tools\\inspect_ctb.py <ctb_file>")
        sys.exit(1)

    inspect_ctb(sys.argv[1])


if __name__ == "__main__":
    main()