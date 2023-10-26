import os
from pathlib import Path
from string import Template
from typing import Dict, List, Optional

from invoke.context import Context
from invoke.tasks import task


def parse_dep5_file(source: Path) -> Dict[str, List[Dict[str, str]]]:
    deps: Dict[str, List[Dict[str, str]]] = {}
    section: Optional[str] = None

    with open(source, "r") as file:
        for line in file:
            if line.startswith("# "):
                section = line[len("# ") : -1].lower()

            if section is None:
                continue

            if line.startswith("Files: "):
                if section not in deps:
                    deps[section] = []

                deps[section].append({"files": line[len("Files: ") : -1]})

            elif line.startswith("Copyright: "):
                if section not in deps:
                    deps[section] = []

                date_author = line[len("Copyright: ") : -1].split(" ")
                date_author.pop(0)
                deps[section][-1]["author"] = " ".join(date_author)

            elif line.startswith("License: "):
                if section not in deps:
                    deps[section] = []

                deps[section][-1]["license"] = line[len("License: ") : -1]

            elif line.startswith("Source: "):
                if section not in deps:
                    deps[section] = []

                deps[section][-1]["source"] = line[len("Source: ") : -1]

    return deps


def generate_credits_file(deps: Dict[str, List[Dict[str, str]]], output: Path) -> None:
    if deps:
        template = Template(
            (
                '- "[$files]($source)" by **$author** licensed'
                " under [$license](./LICENSES/$license.txt)\n"
            )
        )

        with open(output, "w+") as file:
            file.writelines("# Credits\n\n")

            for key, value in deps.items():
                file.writelines(f"## {key.title()}\n")
                for dep in value:
                    file.writelines(template.substitute(**dep))
    else:
        if os.path.exists(output):
            os.remove(output)


@task(
    help={
        "dep5_file": "A path to a dep5 file. (default: .reuse/dep5)",
        "output": "A path for the output credit file. (default: CREDITS.md)",
    },
    optional=["dep5_file", "output"],
)
def generate_credits(
    c: Context, dep5_file: Path = Path(".reuse/dep5"), output: Path = Path("CREDITS.md")
) -> None:
    """
    Generate a CREDITS.md file.
    """
    deps = parse_dep5_file(dep5_file)
    generate_credits_file(deps, output)
