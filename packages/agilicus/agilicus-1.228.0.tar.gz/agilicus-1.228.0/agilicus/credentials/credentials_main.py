import click


@click.command(name="add-object-credential")
@click.option("--object-id", required=True)
@click.option("--object-type", required=True)
@click.option("--org-id", default=None)
@click.option("--priority", default=None)
@click.option("--purpose", default=None)
@click.pass_context
def cli_command_add_object_credential(ctx, **kwargs):
    pass


all_funcs = [func for func in dir() if "cli_command_" in func]


def add_commands(cli):
    glob = globals()
    for func in all_funcs:
        cli.add_command(glob[func])
