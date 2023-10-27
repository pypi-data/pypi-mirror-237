import click

from testapis import __version__
from testapis.scaffold import create_scaffold


@click.command()
@click.version_option(version=__version__, help="Show version.")
@click.option("-p", "--projectName", type=str, default=None, help="Create demo by project name")
# 老是变，等最后定下来再搞，目前也没啥用
def main(projectName):

    if projectName:
        create_scaffold(projectName)
