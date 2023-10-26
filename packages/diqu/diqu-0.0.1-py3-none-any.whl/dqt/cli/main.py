import rich_click as click

from dqt.cli import common
from dqt.tasks.alert import AlertTask


# dqt
@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
    epilog="Specify one of these sub-commands and you can find more help from there.",
)
@click.version_option(common.VERSION)
@click.pass_context
def dqt(ctx, **kwargs):
    """CLI companion tool to support dq-tools package"""


# dqt alert
@dqt.command(name="alert")
@click.pass_context
@common.common_options
@common.common_logging
def alert(ctx, **kwargs):
    """Alert the incidents"""
    AlertTask(**kwargs).run()
