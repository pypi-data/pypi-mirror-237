from invoke.collection import Collection
from invoke.context import Context
from invoke.tasks import task

from ..command import cmd
from ..config import ConfigWrapper
from . import bump_version, generate_credits


@task()
def add_config_to_github_env(c: Context) -> None:
    """
    Add 'godot_version' and 'game_version' to Github env.
    """
    c.run(f'echo "godot_version={ConfigWrapper.godot_version(c)}" >> $GITHUB_ENV')
    c.run(f'echo "game_version={ConfigWrapper.game_version(c)}" >> $GITHUB_ENV')


@task()
def new(c: Context, project_name: str) -> None:
    """
    Create a new godot game project, based on MechanicalFlower/godot-template.
    """
    cmd(
        c,
        "gh",
        "repo",
        "create",
        project_name,
        "--template",
        "MechanicalFlower/godot-template",
        "--clone",
    )


script_ns = Collection("script")
script_ns.add_task(bump_version.bump_version)
script_ns.add_task(generate_credits.generate_credits)
script_ns.add_task(add_config_to_github_env)
script_ns.add_task(new)
