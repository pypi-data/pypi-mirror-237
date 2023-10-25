"""This would contain all the functions to interact with the underlying terraform manifest files"""
import os
import subprocess
from pathlib import Path

import typer
from typing import Optional


def terraform_cli_command_wrapper(
    command: str,
    terraform_dir: Path | None,
    extra_flags: str | None,
):
    if extra_flags:
        terraform_command = f"{command} {extra_flags}"
    else:
        terraform_command = command

    if not terraform_dir:
        terraform_dir = os.path.join(os.getcwd(), "terraform")

    try:
        subprocess.run(
            terraform_command,
            shell=True,
            check=True,
            cwd=terraform_dir,
            stderr=subprocess.PIPE,
        )
        typer.echo("Terraform Apply command successful!")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Terraform Apply Error: {e}")
        typer.echo(e.stderr.decode())  # Print Terraform error output


def terraform_apply(
    terraform_dir: Optional[Path],
    extra_flags: Optional[str] = None,
) -> None:
    """Wrapper function for the terraform apply command"""

    terraform_cli_command_wrapper("terraform apply",terraform_dir, extra_flags)


def terraform_destroy(terraform_dir: Optional[Path], extra_flags: Optional[str] = None,) -> None:
    """Wrapper function for the terraform destroy command"""

    terraform_cli_command_wrapper("terraform destroy",terraform_dir, extra_flags)


def terraform_init(terraform_dir: Optional[Path], extra_flags: Optional[str] = None) -> None:
    """Wrapper function for the terraform destroy command"""

    terraform_cli_command_wrapper("terraform init", terraform_dir, extra_flags)
