"""The CLI of kthutils"""

import logging
import typer
import typerconf as config
import kthutils.ug
import kthutils.participants

cli = typer.Typer(name="kthutils",
                  help="A collection of tools useful at KTH")

logging.basicConfig(format="kthutils: %(levelname)s: %(message)s")

config.add_config_cmd(cli)
cli.add_typer(kthutils.ug.cli)
cli.add_typer(kthutils.participants.cli)

if __name__ == "__main__":
    cli()
