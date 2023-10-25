# TODO: create s3 bucket and dynamodb for managing terraform state files..

import boto3
import botocore.exceptions
import os
from typing import Dict


def bucket_exists(bucket_name: str, client):
    try:
        client.head_bucket(Bucket=bucket_name)
        return True
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            return False  # Bucket doesn't exist
        else:
            raise e


def create_terraform_s3_backend_bucket(user_config_values) -> str:
    client = boto3.client(
        "s3",
        aws_access_key_id=user_config_values["aws_access_key"],
        aws_secret_access_key=user_config_values["aws_secret_key"],
        region_name=user_config_values["aws_region"],
    )
    bucket_name = "fga-terraform-tfstate-test"
    try:
        if not bucket_exists(bucket_name, client):
            client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": user_config_values["aws_region"]
                },
            )

            # Set bucket permissions
            # s3_client.put_bucket_acl(Bucket=bucket_name, ACL="public-read-write")

            # Enable bucket versioning
            client.put_bucket_versioning(
                Bucket=bucket_name, VersioningConfiguration={"Status": "Enabled"}
            )

        return bucket_name
    except botocore.exceptions.ClientError as e:
        raise e

    # TODO: verify s3 encryption
    # # Enable encryption (example: Server-Side Encryption with AWS Key Management Service)
    # s3.put_bucket_encryption(
    #     Bucket=bucket_name,
    #     ServerSideEncryptionConfiguration={
    #         'Rules': [{
    #             'ApplyServerSideEncryptionByDefault': {
    #                 'SSEAlgorithm': 'aws:kms',
    #                 'KMSMasterKeyID': 'your-kms-key-id'
    #             }
    #         }]
    #     }
    # )


def dynamodb_table_exists(table_name, client):
    try:
        client.describe_table(TableName=table_name)
        return True
    except client.exceptions.ResourceNotFoundException:
        return False


def create_dynamodb_table() -> str:
    client = boto3.client("dynamodb")
    table_name = "fga_terraform_lockid_test"

    if not dynamodb_table_exists(table_name, client):
        try:
            client.create_table(
                TableName=table_name,
                KeySchema=[{"AttributeName": "LockID", "KeyType": "HASH"}],
                AttributeDefinitions=[
                    {"AttributeName": "LockID", "AttributeType": "S"}
                ],
                ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
            )
        except botocore.exceptions.ClientError as e:
            raise e

    return table_name
