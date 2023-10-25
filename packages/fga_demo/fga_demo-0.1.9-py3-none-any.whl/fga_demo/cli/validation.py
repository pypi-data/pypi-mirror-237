"""This contains the methods for validating user inputs from the cli """
import typer
from typer import BadParameter
import boto3
import re


def is_valid_region(region: str) -> bool:
    """Checks whether if a region is a valid aws region

    :param region:
    :return: True if region is valid and false otherwise
    """
    # """"""

    client = boto3.client("ec2")
    current_regions = client.describe_regions(AllRegions=True)["Regions"]

    return region in [region["RegionName"] for region in current_regions]


def is_eks_cluster_name_unique(cluster_name: str) -> bool:
    """Checks whether an eks cluster name doesn't exist in the current AWS Account

    :param cluster_name:
    :return: True if cluster name is not present in the current AWS Account and False otherwise.
    """
    # """"""
    eks = boto3.client("eks")

    return cluster_name not in eks.list_clusters()["clusters"]


def eks_name_pattern_match(cluster_name: str) -> bool:
    """Checks whether the eks cluster name matches the following conditions:

    1. The name can contain only alphanumeric characters (case-sensitive) and hyphens.
    2. It must start with an alphabetic character and can't be longer than 100 characters.

    :param cluster_name:
    :return: True if cluster name matches the two conditions and False otherwise.
    """

    pattern = r"^[a-zA-Z][a-zA-Z0-9-]{0,99}$"
    if re.match(pattern, cluster_name):
        return True
    else:
        return False


def prefix_pattern_match(prefix: str) -> bool:
    """Checks whether the eks cluster name matches the following conditions:

    1. an alphanumeric
    2. 3-11 character limit

    :param prefix:
    :return: True if prefix matches the two conditions and False otherwise.
    """

    pattern = r"^[a-zA-Z0-9]{3,11}$"
    if re.match(pattern, prefix):
        return True
    else:
        return False


def cluster_name_validation(
    cluster: str,
    ctx: typer.Context,
    param: typer.CallbackParam,
) -> str | None:
    """Checks whether cluster name follows the specified AWS EKS cluster naming conventions:

    1. The name can contain only alphanumeric characters (case-sensitive) and hyphens.
    2. It must start with an alphabetic character and can't be longer than 100 characters.
    3. The name must be unique within the AWS Region and AWS account that you're creating the cluster in.

    :param cluster:
    :param ctx:
    :param param:
    :return:
        Cluster name if all the above conditions are True otherwise raises a Bad parameter error
    """

    # Makes sure prompt is not terminated even if after a failed input attempt
    if ctx.resilient_parsing:
        return

    # typer.echo(f"Validating {param.name} name")

    if not (is_eks_cluster_name_unique(cluster) and eks_name_pattern_match(cluster)):
        raise BadParameter(f"Specified cluster name{cluster} is not allowed")

    return cluster


def region_validation(
    region: str,
    ctx: typer.Context,
    param: typer.CallbackParam,
) -> str | None:
    """Validates the user specified region

    :param region:
    :param ctx:
    :param param:
    :return:
        True if region is a valid AWS region otherwise False
    """

    # Makes sure prompt is not terminated even if after a failed input attempt
    if ctx.resilient_parsing:
        return

    # typer.echo(f"Validating {param.name} name")

    if not is_valid_region(region):
        raise BadParameter(f"Specified region: {region} does not exist!")
    return region


def prefix_validation(
    prefix: str,
    ctx: typer.Context,
    param: typer.CallbackParam,
) -> str | None:
    """Validates the user specified prefix

    :param prefix:
    :param ctx:
    :param param:
    :return:
        True if prefix is a valid otherwise False
    """
    """"""

    # Makes sure prompt is not terminated even if after a failed input attempt
    if ctx.resilient_parsing:
        return

    # typer.echo(f"Validating {param.name} name")

    if not prefix_pattern_match(prefix):
        raise BadParameter(
            f"{prefix} must be an alphanumeric with 3-11 character limit!"
        )
    return prefix
