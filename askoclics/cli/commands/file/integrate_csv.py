import click
from askoclics.cli.cli import pass_context, json_loads
from askoclics.cli.decorators import custom_exception, dict_output


@click.command('integrate_csv')
@click.argument("file_id", type=str)
@click.option(
    "--columns",
    help="Comma-separated columns (default to detected columns)",
    type=str
)
@click.option(
    "--headers",
    help="Comma-separated headers (default to file headers)",
    type=str
)
@click.option(
    "--force",
    help="Ignore the content type mismatch (ex: force an integer type when AskOmics detects a text type)",
    is_flag=True
)
@click.option(
    "--custom_uri",
    help="Custom uri",
    type=str
)
@click.option(
    "--external_endpoint",
    help="External endpoint",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, file_id, columns="", headers="", force=False, custom_uri="", external_endpoint=""):
    """Send an integration task for a specified file_id

Output:

    Dictionary of task information
    """
    return ctx.gi.file.integrate_csv(file_id, columns=columns, headers=headers, force=force, custom_uri=custom_uri, external_endpoint=external_endpoint)
