import logging

from click.shell_completion import CompletionItem
from diskcache import Cache

from bresh.handlers.cs import CloudShell
from bresh.handlers.offline_pypi import Pypi

EXPIRE = 60
cache = Cache("~/.bresh/cache")
logger = logging.getLogger(__name__)


def shell_name(ctx, param, incomplete):
    return _get_completions(incomplete, _get_shell_names())


def invalidate_shell_name_cache():
    cache.delete("shell_names")


def package_name(ctx, param, incomplete):
    return _get_completions(incomplete, _get_packages())


def invalidate_package_name_cache():
    cache.delete("pypi_packages")


def resource_name(ctx, param, incomplete):
    return _get_completions(incomplete, _get_resources())


def invalidate_resource_name_cache():
    cache.delete("cs_resources")


def resource_command_name(ctx, param, incomplete):
    return _get_completions(
        incomplete, _get_resource_commands(ctx.params["resource_name"])
    )


def invalidate_resource_command_name_cache(r_name: str):
    cache.delete(f"cs_resource_commands_{r_name}")


def blueprint_full_name(ctx, param, incomplete):
    return _get_completions(incomplete, _get_blueprint_full_names())


def invalidate_blueprint_full_name_cache():
    cache.delete("blueprint_full_names")


def _get_shell_names() -> tuple[str, ...]:
    cache_key = "shell_names"
    names = cache.get(cache_key)
    if not names:
        cs = CloudShell.from_cfg()
        names = tuple(s.name for s in cs.Shell.all())
        cache.set(cache_key, names, expire=EXPIRE)
    return names


def _get_packages() -> tuple[str, ...]:
    cache_key = "pypi_packages"
    packages = cache.get(cache_key)
    if not packages:
        pypi = Pypi.from_cfg()
        packages = tuple(pypi.list())
        cache.set(cache_key, packages, expire=EXPIRE)
    return packages


def _get_resources() -> tuple[str, ...]:
    cache_key = "cs_resources"
    if not (resources := cache.get(cache_key)):
        cs = CloudShell.from_cfg()
        resources = tuple(r.name for r in cs.Resource.all())
        cache.set(cache_key, resources, expire=EXPIRE)
    return resources


def _get_blueprint_full_names() -> tuple[str, ...]:
    cache_key = "blueprint_full_names"
    if not (blueprints := cache.get(cache_key)):
        cs = CloudShell.from_cfg()
        blueprints = tuple(b.full_name for b in cs.Blueprint.all())
        cache.set(cache_key, blueprints, expire=EXPIRE)
    return blueprints


def _get_resource_commands(r_name: str) -> tuple[str, ...]:
    cache_key = f"cs_resource_commands_{r_name}"
    if not (commands := cache.get(cache_key)):
        cs = CloudShell.from_cfg()
        resource = cs.Resource.get(r_name)
        commands = tuple(c.name for c in resource.get_commands())
        cache.set(cache_key, commands, expire=EXPIRE)
    return commands


def _get_completions(incomplete: str, names: tuple[str, ...]) -> tuple[CompletionItem]:
    return tuple(
        CompletionItem(n) for n in names if n.lower().startswith(incomplete.lower())
    )
