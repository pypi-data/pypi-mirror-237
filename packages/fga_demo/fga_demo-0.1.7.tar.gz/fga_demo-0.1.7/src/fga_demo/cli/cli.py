from typing import Optional, Dict
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

from .validation import region_validation, cluster_name_validation, prefix_validation

from .utils import (
    create_project_directory,
    create_terraform_dir,
    ProjectInitializationError,
)

from .terraform_interface import (
    terraform_apply,
    terraform_destroy,
    terraform_init,
)

app = typer.Typer(pretty_exceptions_show_locals=False, pretty_exceptions_enable=False)


@app.command()
def init(
    project_folder_name: str = typer.Option(
        prompt="Provide a project name",
    ),
    region: str = typer.Option(
        default="eu-west-1",
        prompt="What region should your resources be provisioned in? default:",
        callback=region_validation,
    ),
    cluster_name: str = typer.Option(
        default="eks-cluster",
        prompt="What should we name the cluster? default:",
        callback=cluster_name_validation,
    ),
    resource_prefix: Optional[str] = typer.Option(
        default="fga",
        prompt="What resource prefix should we use(an alphanumeric; 3-11 character limit)? default:",
        callback=prefix_validation,
    ),
    access_key: str = typer.Option(
        prompt="Provide the IAM Access Key",
        # confirmation_prompt=True,
        # hide_input=True,
    ),
    secret_key: str = typer.Option(
        prompt="Provide the AWS Secret key",
        # confirmation_prompt=True,
        hide_input=True,
    ),
) -> None:
    """Creates customized FGA project

    :param project_folder_name:
    :param region:
    :param cluster_name:
    :param resource_prefix:
    :param access_key:
    :param secret_key:
    :return:
    """

    # TODO: include a spinner to show task progress bar.
    user_config_values: Dict[str, str | None] = {
        "eks_cluster_name": cluster_name,
        "aws_region": region,
        "aws_access_key": access_key,
        "aws_secret_key": secret_key,
        "aws_resource_prefix": resource_prefix,
    }

    
    try :
        working_directory = create_project_directory(project_folder_name)
    except ProjectInitializationError:
        typer.echo("Project folder initialization fails")
        typer.Abort()


    create_terraform_dir(working_directory, user_config_values)


    # initializes undelying terraform code
    terraform_init(extra_flags="-backend-config=backend.hcl")

    typer.echo(
        f"Your project {project_folder_name} has been created here: {working_directory}"
    )
   


@app.command()
def provision() -> None:
    """Provision the terraform resources...

    :return:
    """

    # Summary and confirmation prompt before running the apply command
    # TODO: show the resource summary
    confirm = typer.confirm(
        f"The following resources will be provisioned..., do you want to continue?"
    )
    if not confirm:
        raise typer.Abort()

    typer.echo("This may take a while...approx 20 mins")
    terraform_apply(extra_flags="--auto-approve")


@app.command()
def destroy() -> None:
    """Runs a terraform destroy command, to destroy all provisioned resources

    :return:
    """
    # TODO: add a summary to this
    confirm = typer.confirm(
        f"The following resources will be destroyed..., do you want to continue?"
    )
    if not confirm:
        raise typer.Abort()

    typer.echo("Destroying all the resources...")
    terraform_destroy(extra_flags="--auto-approve")


if __name__ == "__main__":
    app()
