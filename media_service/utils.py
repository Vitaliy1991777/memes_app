import boto3
from botocore.exceptions import NoCredentialsError
from fastapi import UploadFile

def upload_file_to_s3(file: UploadFile):
    s3 = boto3.client("s3", aws_access_key_id="ACCESS_KEY", aws_secret_access_key="SECRET_KEY")

    try:
        s3.upload_fileobj(file.file, "my-bucket", file.filename)
        return f"https://my-bucket.s3.amazonaws.com/{file.filename}"
    except NoCredentialsError:
        raise NoCredentialsError
