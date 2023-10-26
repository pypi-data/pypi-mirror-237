from __future__ import annotations

import click

from bresh.handlers.cs import CloudShell
from bresh.handlers.resource import Resource, ResourceNotFound, Command, CommandNotFound


def get_resource(cs: CloudShell, name: str) -> Resource:
    try:
        resource = cs.Resource.get(name)
    except ResourceNotFound:
        raise click.UsageError(f"Resource '{name}' not found")
    return resource


def get_command(resource: Resource, name: str) -> Command:
    try:
        command = resource.get_command(name)
    except CommandNotFound:
        raise click.UsageError(
            f"Command '{name}' not found for resource '{resource.name}'"
        )
    return command


def get_command_kwargs(command: Command) -> dict[str, str]:
    e = click.UsageError("Command parameter should be passed as --param-name value")
    passed_args = click.get_current_context().args

    param_names = passed_args[::2]
    param_values = passed_args[1::2]

    # check that all parameters have values
    if len(param_names) != len(param_values):
        raise e

    for i, name in enumerate(param_names[:]):
        # check that parameter name starts with '--'
        if not name.startswith("--"):
            raise e
        name = name[2:]  # remove leading '--'

        for param in command.parameters:
            # check that parameter name is valid
            if param.name == name or param.name == name.replace("-", "_"):
                param_names[i] = param.name
                value = param_values[i]

                # check parameter value is in allowed values
                if param.allowed_values and value not in param.allowed_values:
                    raise click.UsageError(
                        f"Unknown value '{value}' for parameter '{param.name}'. "
                        f"Allowed values: {param.allowed_values}"
                    )
                break
        else:
            raise click.UsageError(f"Unknown command parameter '{name}'")

    kwargs = dict(zip(param_names, param_values))
    return kwargs
