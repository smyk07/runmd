# import packages
from typing import Annotated, Optional
import typer
import subprocess

# import runmd
from runmd import runmd


def main(file: Annotated[Optional[str], typer.Argument()] = None):
    if file:
        # run smth when a filepath is given
        runmd(file)
    else:
        try:
            file = subprocess.check_output(
                "find ./ -mindepth 0 | fzf", executable="/bin/bash", shell=True
            ).decode("utf-8")
        except subprocess.CalledProcessError:
            exit()

        runmd(file)


if __name__ == "__main__":
    typer.run(main)
