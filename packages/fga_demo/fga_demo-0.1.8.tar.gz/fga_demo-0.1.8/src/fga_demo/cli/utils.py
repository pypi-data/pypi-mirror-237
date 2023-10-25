from typing import Optional, Dict
from pathlib import Path
import os
import site
import shutil

from .state_manager import (
    create_dynamodb_table,
    create_terraform_s3_backend_bucket,
)

from .terraform_interface import terraform_init

import typer


class ProjectInitializationError(Exception):
    "raised when project folder fails to initialize"
    

def create_project_directory(project_name: str) -> Path:
    """create a project directory"""
    project_dir = Path(os.path.join(os.getcwd(), project_name))

    if project_dir.exists():
        # The directory already exists, ask the user if they want to update it
        confirm = typer.confirm(
            f"The {project_name} directory already exists. Do you want to update its contents?"
        )
        if not confirm:
            return project_dir  # Return the existing directory without changes

        # If the user confirms, remove the existing directory
        try:
            shutil.rmtree(project_dir)
        except OSError as e:
            typer.echo(f"Error removing directory: {e}")
            return project_dir
        
    try:
        project_dir.mkdir(parents=True)
    except ( OSError) as e:
        typer.echo(f"Error creating directory: {e}")
        raise ProjectInitializationError

    return project_dir


def create_terraform_dir(working_dir, user_config_values) -> Path:
    """This copies the terraform modules from the site-packages
    and creates a terraform directory in the project directory..."""

    terraform_dir = Path(os.path.join(working_dir, "terraform"))

    if not os.path.exists(terraform_dir):
        site_packages_dir = site.getsitepackages()[0]
        directory_contents = os.listdir(site_packages_dir)
        search_key = "fga_demo"

        if search_key not in directory_contents:
            typer.echo(
                "No terraform modules found. Make sure you've activated the fga virtual environment"
            )
            raise typer.Abort()
        else:
            source_directory = os.path.join(site_packages_dir, search_key, "terraform")
            try:
                # recursive_copy to terraform directory
                shutil.copytree(source_directory, terraform_dir)
                # typer.echo(f"{search_key} folder ready")
            except FileExistsError:
                confirm = typer.confirm(
                    f"The terraform directory already exists in {working_dir} Do you want to update its contents?"
                )
                if not confirm:
                    return (
                        terraform_dir  # Return the existing directory without changes
                    )
                shutil.copytree(source_directory, terraform_dir, dirs_exist_ok=True)


    create_tfvars_file(terraform_dir, user_config_values)

    # configure remote backend for terraform
    s3_backend_bucket_name = create_terraform_s3_backend_bucket(user_config_values)
    dynamodb_table_name = create_dynamodb_table()

    create_backend_hcl_file(
        s3_backend_bucket_name,
        dynamodb_table_name,
        user_config_values["aws_region"],
        terraform_dir,
    )

    try:
        # initializes undelying terraform code
        terraform_init(extra_flags="-backend-config=backend.hcl")
    except FileNotFoundError:
        typer.echo(f"Error running terraform init, Make sure you're in this {working_dir}")
        raise typer.Abort()


def create_tfvars_file(
    working_dir: Path,
    user_config_values: Dict[str, str],
) -> None:
    tfvars_path = working_dir / "terraform.tfvars"

    if tfvars_path.is_file():
        # The file already exists, ask the user if they want to update it
        confirm = typer.confirm(
            f"The file '{tfvars_path.relative_to(Path.cwd())}' already exists. Do you want to update its contents?"
        )
        if not confirm:
            typer.echo("File not updated.")
            return

    # Populates dictionary values into the created terraform.tfvars file
    try:
        with open(tfvars_path, "w") as f:
            for key, value in user_config_values.items():
                f.write(f'{key} = "{value}"\n')
    except Exception as e:
        typer.echo(f"Error creating or updating the file: {e}")


def create_backend_hcl_file(
    s3_bucket_name: str,
    dynamodb_table_name: str,
    region_name: str,
    working_dir: Path,
):
    data = {
        "region": region_name,
        "bucket": s3_bucket_name,
        "key": "state/terraform.tfstate",
        "dynamodb_table": dynamodb_table_name,
    }

    try:
        file_path = os.path.join(working_dir, "backend.hcl")

        # Create the HCL file
        with open(file_path, "w") as f:
            for key, value in data.items():
                f.write(f'{key} = "{value}"\n')
    except FileNotFoundError as e:
        typer.echo(f"backend.hcl not created: {e}")

