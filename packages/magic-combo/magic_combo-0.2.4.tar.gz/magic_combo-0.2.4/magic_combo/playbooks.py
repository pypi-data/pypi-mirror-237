from typing import Optional

from invoke.collection import Collection
from invoke.context import Context
from invoke.tasks import task

from .tasks import (
    clean_combo,
    clean_godot,
    clean_plug,
    export_release_linux,
    export_release_mac,
    export_release_windows,
    import_resources,
    install_addons,
    install_godot,
    install_templates,
    run_release,
)


@task(pre=[clean_combo, clean_godot, clean_plug])
def clean(c: Context) -> None:
    """
    Clean combo, godot and plug caches.
    """
    pass


@task(
    pre=[
        clean_godot,
        clean_plug,
        install_godot,
        install_templates,
        install_addons,
        import_resources,
        export_release_linux,
    ]
)
def build(c: Context) -> None:
    """
    Build godot game for Linux.
    """
    pass


@task(pre=[build, run_release])
def run(c: Context) -> None:
    """
    Build and run godot game for Linux.
    """
    pass


@task(
    help={
        "platforms": "Comma separated list of platform to export",
        "all": "Export to all platform",
    },
    optional=["platform", "all"],
)
def export(
    c: Context, platforms: Optional[str] = None, all: Optional[bool] = None
) -> None:
    """
    Release export for any platform.
    """
    if all:
        platforms = "windows,linux,mac"

    if platforms:
        for platform in platforms.split(","):
            if platform.strip().lower() == "linux":
                export_release_linux(c)
            elif platform.strip().lower() == "windows":
                export_release_windows(c)
            elif platform.strip().lower() == "mac":
                export_release_mac(c)


playbook_ns = Collection("playbook")
playbook_ns.add_task(clean)
playbook_ns.add_task(build)
playbook_ns.add_task(run)
playbook_ns.add_task(export)
