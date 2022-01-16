import subprocess

import click

# docker-compose exec website siapp cov
# docker-compose exec website siapp cov --help

@click.command()
@click.argument('path', default='siapp')
def cli(path):
    """
    Run a test coverage report.

    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = 'py.test --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)
