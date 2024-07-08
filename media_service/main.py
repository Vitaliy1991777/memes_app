from fastapi import FastAPI, File, UploadFile
import boto3
from botocore.exceptions import NoCredentialsError
from .utils import upload_file_to_s3

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        url = upload_file_to_s3(file)
        return {"url": url}
    except NoCredentialsError:
        return {"error": "Credentials not available"}
