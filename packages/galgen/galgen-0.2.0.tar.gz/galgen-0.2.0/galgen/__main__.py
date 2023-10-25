import click
import coloredlogs
from galgen import UserError
from galgen.init import init_action
from galgen.build import build_action
from logging import getLogger

coloredlogs.install(level='INFO', fmt='%(message)s')

logger = getLogger(__file__)

@click.group
def main():
    """Simple gallery generator."""
    pass

@main.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('-f', '--force', default=False, is_flag=True, help='Overwrite existing files')
def init(path, force):
    """Generate config files."""
    try:
        init_action(path, force)
    except UserError as exc:
        logger.critical(str(exc))

@main.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('-o', '--open', 'show', default=False, is_flag=True, help='Open gallery in the browser')
@click.option('-f', '--force', default=False, is_flag=True, help='Overwrite existing files')
def build(path, force, show):
    """Generate webpage."""
    try:
        build_action(path, force, show)
    except UserError as exc:
        logger.critical(str(exc))

if __name__ == '__main__':
    main()
