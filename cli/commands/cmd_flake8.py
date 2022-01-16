import subprocess

import click

# docker-compose exec website siapp flake8 --help
# docker-compose exec website siapp flake8

@click.command()
@click.option('--skip-init/--no-skip-init', default=True,
              help='Skip __init__.py files?')
@click.argument('path', default='siapp')
def cli(skip_init, path):
    """
    Run flake8 to analyze your code base.

    :param skip_init: Skip checking __init__.py files
    :param path: Test coverage path
    :return: Subprocess call result
    """
    flake8_flag_exclude = ''

    if skip_init:
        flake8_flag_exclude = ' --exclude __init__.py'

    cmd = 'flake8 {0}{1}'.format(path, flake8_flag_exclude)
    return subprocess.call(cmd, shell=True)
