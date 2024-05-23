import boto3

s3 = boto3.client('s3', region_name='region_name')
s3.upload_file(f'path of file', 'bucket name', f'path in s3 bucket')