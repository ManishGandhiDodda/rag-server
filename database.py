import os
from dotenv import load_dotenv
from supabase import create_client, Client
import boto3

load_dotenv()

sb_url = os.getenv("SUPABASE_API_URL")
sb_key = os.getenv("SUPABASE_SERVICE_KEY")

if not sb_url or not sb_key:
    raise ValueError("Missing Supabase Details")

supabase: Client = create_client(supabase_url=sb_url,supabase_key=sb_key)

# S3 Setup

s3_client = boto3.client("s3",
                         endpoint_url=os.getenv('AWS_ENDPOINT_URL_S3'),
                         aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                         aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                         region_name=os.getenv('AWS_REGION'))

BUCKET_NAME = os.getenv('S3_BUCKET_NAME')