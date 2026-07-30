"""
LithoForge

Copyright (c) 2026 Benjamin Lloyd and Contributors

Licensed under the MIT License.
See LICENSE for details.
"""

from pathlib import Path


def inspect_ctb(filename):
    """Read a CTB file and print basic information."""

    path = Path(filename)

    if not path.exists():
        print(f"Error: '{filename}' not found.")
        return

    file_size = path.stat().st_size

    print(f"File: {path.name}")
    print(f"Size: {file_size:,} bytes")

    with path.open("rb") as file:
        header = file.read(64)

    print("\nFirst 64 bytes:")

    for i in range(0, len(header), 16):
        chunk = header[i:i + 16]
        hex_string = " ".join(f"{byte:02X}" for byte in chunk)
        print(f"{i:04X}: {hex_string}")


if __name__ == "__main__":
    inspect_ctb("samples/mars3/mars3_10mm_square.ctb")
