from pathlib import Path
from typing import Any, Iterable

from invoke.context import Context

from .config import ConfigWrapper
from .constants import COMBO_BIN_PATH

String = str | Path


def cmd(c: Context, command: String, *arguments: String) -> Any:
    builder = CommandBuilder(c)
    if command == "godot":
        builder = builder.godot()
    else:
        builder = builder.cmd(command)
    builder = builder.args(*arguments)
    return builder.run()


class CommandBuilder:
    def __init__(self, c: Context) -> None:
        self.c = c
        self._args: Iterable[str] = []
        self._cmd: str = ""

    def run(self) -> Any:
        return self.c.run(" ".join([self._cmd, *self._args]))

    def cmd(self, cmd: String) -> "CommandBuilder":
        self._cmd = str(cmd)
        return self

    def godot(self) -> "CommandBuilder":
        return self.cmd(COMBO_BIN_PATH / ConfigWrapper.godot_filename(self.c))

    def args(self, *args: String) -> "CommandBuilder":
        self._args = [str(arg) for arg in args]
        return self
