from __future__ import annotations

from pathlib import Path

import click
import humanize

from bresh import __version__
from bresh.config import BreshCfg
from bresh.handlers.cs import CloudShell
from bresh.handlers.offline_pypi import Pypi
from bresh.handlers.package import build_package
from bresh.handlers.resource import ResourceNotReserved
from bresh.handlers.shellfoundry import Shellfoundry
from bresh.utils import complete

from rich.console import Console
from rich.table import Table
from rich import print as rprint

import logging

from bresh.utils.cli_utils import get_resource, get_command, get_command_kwargs
from bresh.utils.complete import invalidate_package_name_cache
from bresh.utils.progress_bar import spinner

logger = logging.getLogger("bresh")
logger.setLevel(logging.INFO)
hdr = logging.StreamHandler()
logger.addHandler(hdr)


@click.group()
@click.version_option(__version__)
def cli():
    pass


@cli.group("config")
def config_group():
    pass


@config_group.command("show")
def show_config():
    from dynaconf.vendor import tomllib

    cfg = BreshCfg.load()
    toml = tomllib.dumps(cfg.get_full_dict())
    rprint(toml)


@config_group.command("set")
@click.argument("name")
@click.argument("value")
def set_config(name: str, value: str):
    cfg = BreshCfg.load()
    storage = cfg
    try:
        storage_path, name = name.lower().rsplit(".", 1)
    except ValueError:
        name = name.lower()
    else:
        for key in storage_path.split("."):
            storage = getattr(storage, key)

    setattr(storage, name, value)
    cfg.save()


@config_group.command("name")
def show_config_name():
    name = BreshCfg.get_cfg_name()
    rprint(name)


@config_group.command("list")
def list_configs():
    names = BreshCfg.get_cfg_names()
    console = Console()
    table = Table(title="Configs")
    table.add_column("Name", style="cyan")
    for name in names:
        table.add_row(name)
    console.print(table)


@config_group.command("use")
@click.argument("name")
def use_config(name: str):
    BreshCfg.set_cfg_name(name)


@config_group.command("new")
@click.argument("name")
@click.option("--from", "from_", required=False)
def new_config(name: str, from_: str | None):
    assert name not in BreshCfg.get_cfg_names()
    BreshCfg.new_cfg(name, from_)


@cli.group("pypi")
def pypi_group():
    pass


@pypi_group.command("list")
def pypi_list():
    pypi = Pypi.from_cfg()
    rprint("\n".join(pypi.list()))


@pypi_group.command("upload")
@click.argument(
    "paths",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    nargs=-1,
)
def pypi_upload(paths: tuple[Path, ...]) -> None:
    if not paths:
        raise click.UsageError("Please specify at least one package to upload")
    pypi = Pypi.from_cfg()
    pypi.upload_packages(*paths)


@pypi_group.command("clear")
def pypi_clear():
    pypi = Pypi.from_cfg()
    pypi.clear()
    invalidate_package_name_cache()


@pypi_group.command("delete")
@click.argument("names", nargs=-1, shell_complete=complete.package_name)
def pypi_delete(names: tuple[str, ...]) -> None:
    if not names:
        raise click.UsageError("Please specify at least one package to delete")
    pypi = Pypi.from_cfg()
    pypi.delete_packages(*names)
    invalidate_package_name_cache()


@pypi_group.command("build")
@click.argument(
    "paths", nargs=-1, type=click.Path(exists=True, file_okay=False, path_type=Path)
)
@click.option("--build-num", "-b", is_flag=True, default=False)
@click.option("--upload", "-u", is_flag=True, default=False)
@click.option(
    "--dist", "-d", type=click.Path(file_okay=False, path_type=Path), default=None
)
@click.option("--verbose", "-v", is_flag=True, default=False)
def package_build(
    paths: tuple[Path, ...],
    build_num: bool,
    upload: bool,
    dist: Path | None,
    verbose: bool,
):
    if not paths:
        paths = [Path.cwd()]
    for path in paths:
        new_packages = build_package(path, dist, build_num, quiet=not verbose)
        for p in new_packages:
            if p.suffix == ".whl":
                packages_to_upload = {p}
                break
        else:
            packages_to_upload = new_packages

        names = ", ".join(p.name for p in packages_to_upload)
        logger.info(f"Built files: {names}")
        if upload:
            pypi = Pypi.from_cfg()
            pypi.upload_packages(*packages_to_upload)


@cli.group("shell")
def shell_group():
    pass


@shell_group.command("list")
def shell_list():
    cs = CloudShell.from_cfg()
    console = Console()
    table = Table(title="Shells")
    table.add_column("Name", style="cyan")
    table.add_column("Version", style="magenta")
    table.add_column("Official")
    for s in cs.Shell.all():
        official = "[green]Yes" if s.is_official else "[red]No"
        table.add_row(s.name, s.version, official)

    console.print(table)


@shell_group.command("download")
@click.argument("name", shell_complete=complete.shell_name)
def shell_download(name: str):
    cs = CloudShell.from_cfg()
    shell = cs.Shell.get(name)
    shell.download(Path.cwd())


@shell_group.command("upload")
@click.argument("path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
def shell_upload(path: Path):
    cs = CloudShell.from_cfg()
    cs.Shell.upload(path)
    complete.invalidate_shell_name_cache()


@shell_group.command("reload")
@click.argument("name", shell_complete=complete.shell_name)
def shell_reload(name: str):
    cs = CloudShell.from_cfg()
    shell = cs.Shell.get(name)
    shell.reload()


@shell_group.command("delete")
@click.argument("name", shell_complete=complete.shell_name)
def shell_delete(name: str):
    cs = CloudShell.from_cfg()
    shell = cs.Shell.get(name)
    shell.delete()
    complete.invalidate_shell_name_cache()


@shell_group.command("install")
@click.argument(
    "paths", nargs=-1, type=click.Path(exists=True, file_okay=False, path_type=Path)
)
def shell_install(paths: tuple[Path, ...]):
    if not paths:
        paths = [Path.cwd()]
    shellfoundry = Shellfoundry.from_cfg()
    for path in paths:
        print(f"Installing shell {path.name}")
        shellfoundry.install(path)


@cli.group("resource")
def resource_group():
    pass


@resource_group.command("list")
def resource_list():
    cs = CloudShell.from_cfg()
    console = Console()
    table = Table(title="Resources")
    table.add_column("Name", style="cyan")
    table.add_column("Address", style="magenta")
    table.add_column("Model")
    table.add_column("Reserved")
    for r in cs.Resource.all():
        reserved = "[green]Yes" if r.in_active_sandbox else "[red]No"
        table.add_row(r.name, r.address, r.model, reserved)

    console.print(table)


@resource_group.command("reserve")
@click.argument("names", shell_complete=complete.resource_name, nargs=-1)
def resource_reserve(names: tuple[str, ...]):
    if not names:
        raise click.UsageError("Please specify at least one resource to reserve")

    cs = CloudShell.from_cfg()
    resources = [get_resource(cs, name) for name in names]

    for resource in resources:
        assert not resource.in_active_sandbox

    sandbox_name = ", ".join(r.name for r in resources)
    sandbox = cs.Sandbox.create(sandbox_name, wait=True)
    sandbox.add_resource(*resources)

    rprint(f"[green]Sandbox [blue]{sandbox.name}[/blue] created")


@resource_group.command("autoload")
@click.argument("name", shell_complete=complete.resource_name)
def resource_autoload(name: str):
    cs = CloudShell.from_cfg()
    resource = get_resource(cs, name)
    with spinner():
        resource.autoload()


@resource_group.command(
    name="execute",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
    help=(
        "You can pass parameters as --param-name value. "
        "Or they will be asked interactively."
    ),
)
@click.argument("resource_name", shell_complete=complete.resource_name)
@click.argument("command_name", shell_complete=complete.resource_command_name)
def resource_execute(resource_name: str, command_name: str):
    cs = CloudShell.from_cfg()
    resource = get_resource(cs, resource_name)
    command = get_command(resource, command_name)
    # get command parameters from command line
    kwargs = get_command_kwargs(command)

    if not kwargs:
        # get command parameters interactively
        for param in command.parameters:
            rprint(param)
            type_ = click.Choice(param.allowed_values) if param.allowed_values else None
            out = click.prompt(param.name, default=param.default, type=type_)
            kwargs[param.name] = out

    try:
        res = resource.execute(command_name, **kwargs)
    except ResourceNotReserved:
        raise click.UsageError(f"Resource '{resource_name}' should be reserved")
    else:
        rprint(res)


@resource_group.command("delete")
@click.argument("name", shell_complete=complete.resource_name)
def resource_delete(name: str):
    cs = CloudShell.from_cfg()
    resource = get_resource(cs, name)
    resource.delete()
    complete.invalidate_resource_name_cache()


@resource_group.group("command")
def resource_command_group():
    pass


@resource_command_group.command("list")
@click.argument("resource_name", shell_complete=complete.resource_name)
def resource_list_commands(resource_name: str):
    cs = CloudShell.from_cfg()
    resource = get_resource(cs, resource_name)

    table = Table(title=f"Commands of the resource [red]{resource_name}[/red]")
    table.add_column("Name", style="cyan")
    table.add_column("Description", style="magenta")

    for command in resource.get_commands():
        table.add_row(command.name, command.description)

    console = Console()
    console.print(table)


@resource_command_group.command("show")
@click.argument("resource_name", shell_complete=complete.resource_name)
@click.argument("command_name", shell_complete=complete.resource_command_name)
def resource_show_command(resource_name: str, command_name: str):
    cs = CloudShell.from_cfg()
    resource = get_resource(cs, resource_name)
    command = get_command(resource, command_name)

    console = Console()

    if not command.parameters:
        console.print(
            f"Command [blue]{command_name}[/blue] of the "
            f"resource [red]{resource_name}[/red] has no parameters"
        )
        return

    table = Table(
        title=f"Parameters of the command [blue]{command_name}[/blue] of the "
        f"resource [red]{resource_name}[/red]"
    )
    table.add_column("Name", style="cyan")
    table.add_column("Mandatory", style="magenta")
    table.add_column("Default value", style="magenta")
    table.add_column("Description", style="magenta")
    table.add_column("Allowed Values", style="magenta")

    for param in command.parameters:
        allowed_values = ", ".join(param.allowed_values) if param.allowed_values else ""
        table.add_row(
            param.name,
            "[green]Yes" if param.mandatory else "[red]No",
            param.default,
            param.description,
            allowed_values,
        )

    console.print(table)


@cli.group("blueprint")
def blueprint_group():
    pass


@blueprint_group.command("list")
def blueprint_list():
    cs = CloudShell.from_cfg()
    console = Console()
    table = Table(title="Blueprints")
    table.add_column("Full Name", style="cyan")
    for b in cs.Blueprint.all():
        table.add_row(b.full_name)
    console.print(table)


@blueprint_group.command("start")
@click.argument("full-name", shell_complete=complete.blueprint_full_name)
@click.option("--wait", "-w", is_flag=True, default=False)
@click.option("--duration", "-d", type=int, default=120)
def blueprint_start(full_name: str, wait: bool, duration: int):
    cs = CloudShell.from_cfg()
    sandbox = cs.Sandbox.create(full_name, full_name, duration=duration, wait=wait)
    click.echo(sandbox.id)


@cli.group("sandbox")
def sandbox_group():
    pass


@sandbox_group.command("list")
def sandbox_list():
    cs = CloudShell.from_cfg()
    console = Console()
    table = Table(title="Sandboxes")
    table.add_column("Name", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Ending in", style="magenta")
    table.add_column("ID", style="green")
    for s in cs.Sandbox.get_alive():
        end_in = humanize.precisedelta(s.time_left, minimum_unit="hours", format="%0d")
        table.add_row(s.name, s.status.value, end_in, s.id)
    console.print(table)


@cli.command("add-autocomplete", help="Add autocomplete to zshrc")
def add_autocomplete():
    text = """
### Added by bresh  ###
eval "$(_BRESH_COMPLETE=zsh_source bresh)"
### End bresh ###
"""
    zshrc = Path.home() / ".zshrc"
    if text in zshrc.read_text():
        rprint("Already added")
    else:
        with zshrc.open("a") as f:
            f.write(text)
        rprint("Added. Please restart your shell.")


if __name__ == "__main__":
    cli()
