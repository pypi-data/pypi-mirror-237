import sys
from typing import Any, Dict

from invoke.collection import Collection
from invoke.config import Config
from invoke.program import Program

from .playbooks import playbook_ns
from .scripts import script_ns
from .tasks import task_ns


class ComboConfig(Config):
    prefix = "combo"

    @staticmethod
    def global_defaults() -> Dict[str, Any]:
        return {
            **Config.global_defaults(),
            "godot": {
                "version": "4.1.2",
                "release": "stable",
                "subdir": "",
                "platform": "linux.x86_64",
            },
            "game": {
                "name": None,
                "version": "0.1.0",
            },
        }


def main() -> None:
    ns = Collection(playbook_ns, task_ns, script_ns)
    program = Program(version="0.2.4", namespace=ns, config_class=ComboConfig)
    program.run()
    sys.exit(0)


main()
