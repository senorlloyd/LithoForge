"""
LithoForge

Copyright (c) 2026 Benjamin Lloyd and Contributors

Licensed under the MIT License.
See LICENSE for details.
"""

import struct
import sys
from pathlib import Path


def inspect_ctb(filename):
    path = Path(filename)

    if not path.exists():
        print(f"Error: '{filename}' not found.")
        return

    print("=" * 68)
    print("LithoForge CTB Inspector")
    print("=" * 68)

    print(f"File : {path.name}")
    print(f"Size : {path.stat().st_size:,} bytes")

    with path.open("rb") as file:
        header = file.read(128)

    print("\nHeader Analysis\n")

    print(f"{'Offset':<10}{'Hex Bytes':<20}{'UInt32':>12}")
    print("-" * 44)

    for offset in range(0, len(header), 4):

        chunk = header[offset:offset + 4]

        if len(chunk) < 4:
            break

        value = struct.unpack("<I", chunk)[0]

        hex_string = " ".join(f"{b:02X}" for b in chunk)

        print(f"0x{offset:04X}   {hex_string:<20}{value:>12,}")


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python tools\\inspect_ctb.py <ctb_file>")
        sys.exit(1)

    inspect_ctb(sys.argv[1])


if __name__ == "__main__":
    main()