import boto3
from loguru import logger



s3 = boto3.client('s3', region_name='region_name')
BUCKET_NAME = 's3_name'
s3.download_file(BUCKET_NAME, 'file_path', 'Path_store_in_s3')

