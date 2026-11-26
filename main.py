import os
from pathlib import Path


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    expected = b"lore\n"
    output_file.write_bytes(expected)
    if output_file.read_bytes() != expected:
        raise AssertionError("entry.txt does not contain the expected bytes")


if __name__ == "__main__":
    main()
