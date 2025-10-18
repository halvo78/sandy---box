_# data_lake_poc.py

import boto3
import os

# --- Configuration ---
SPACES_ACCESS_KEY = os.getenv("SPACES_ACCESS_KEY", "DO00TTQK2AVC9DBZQ74V")
SPACES_SECRET_KEY = os.getenv("SPACES_SECRET_KEY", "Pp2EZ5ZIQZkHvnR0CEU5zAPv59XaX4yLUD+ISu4Cjuc")
SPACES_ENDPOINT_URL = os.getenv("SPACES_ENDPOINT_URL", "https://nyc3.digitaloceanspaces.com")
SPACES_REGION = os.getenv("SPACES_REGION", "us-east-1")

# --- Create a boto3 session ---
session = boto3.session.Session()
client = session.client(
    "s3",
    region_name=SPACES_REGION,
    endpoint_url=SPACES_ENDPOINT_URL,
    aws_access_key_id=SPACES_ACCESS_KEY,
    aws_secret_access_key=SPACES_SECRET_KEY,
)

def list_buckets():
    """List all buckets."""
    try:
        response = client.list_buckets()
        print("--- Bucket List Response ---")
        print(response)
        print("--------------------------")
        print("Buckets:")
        for bucket in response["Buckets"]:
            print(f"  - {bucket['Name']}")
    except Exception as e:
        print(f"Error listing buckets: {e}")

def upload_file(bucket_name, file_path, object_name=None):
    """Upload a file to a bucket."""
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        with open(file_path, "rb") as f:
            client.upload_fileobj(f, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name} successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def list_objects(bucket_name):
    """List all objects in a bucket."""
    try:
        response = client.list_objects(Bucket=bucket_name)
        print(f"Objects in bucket {bucket_name}:")
        if 'Contents' in response:
            for obj in response["Contents"]:
                print(f"  - {obj['Key']}")
        else:
            print("  No objects found.")
    except Exception as e:
        print(f"Error listing objects: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("This is a sample file for the data lake proof of concept.")

    BUCKET_NAME = "lyratradingbucket"

    print("--- Data Lake Proof of Concept ---")
    list_buckets()
    upload_file(BUCKET_NAME, "sample.txt")
    list_objects(BUCKET_NAME)
    print("----------------------------------")

