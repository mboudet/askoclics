import click
from askoclics.cli.cli import pass_context, json_loads
from askoclics.cli.decorators import custom_exception, dict_output


@click.command('integrate_gff')
@click.argument("file_id", type=str)
@click.option(
    "--entities",
    help="Comma-separated list of entities to integrate. (Default to all available entities)",
    type=str
)
@click.option(
    "--custom_uri",
    help="Custom uri",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, file_id, entities="", custom_uri=""):
    """Send an integration task for a specified file_id

Output:

    Dictionary of task information
    """
    return ctx.gi.file.integrate_gff(file_id, entities=entities, custom_uri=custom_uri)
