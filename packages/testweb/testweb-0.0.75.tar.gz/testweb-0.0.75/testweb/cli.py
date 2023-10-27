import click
import subprocess

from testweb import __version__
from testweb.scaffold import create_scaffold


@click.command()
@click.version_option(version=__version__, help="Show version.")
@click.option("-i", "--install", is_flag=True, help="Install the browser driver.")
@click.option("-p", "--projectName", type=str, default=None, help="Create demo by project name")
# 老是变，等最后定下来再搞，目前也没啥用
def main(install, projectName):
    if install:
        subprocess.run(["playwright", "install"])

    if projectName:
        create_scaffold(projectName)
