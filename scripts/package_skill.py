"""Package a skill folder into a .skill file (tar.gz archive)."""

import argparse
import os
import sys
import tarfile
from pathlib import Path


def package_skill(skill_path: str) -> str:
    skill_dir = Path(skill_path).resolve()

    if not skill_dir.is_dir():
        print(f"Error: {skill_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print(f"Error: {skill_md} not found", file=sys.stderr)
        sys.exit(1)

    skill_name = skill_dir.name
    output_file = skill_dir.parent / f"{skill_name}.skill"

    with tarfile.open(output_file, "w:gz") as tar:
        for root, dirs, files in os.walk(skill_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = str(file_path.relative_to(skill_dir.parent))
                tar.add(file_path, arcname=arcname)

    print(f"Packaged: {output_file}")
    return str(output_file)


def main():
    parser = argparse.ArgumentParser(description="Package a skill folder into a .skill file")
    parser.add_argument("skill_path", help="Path to the skill folder")
    args = parser.parse_args()
    package_skill(args.skill_path)


if __name__ == "__main__":
    main()
