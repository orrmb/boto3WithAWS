import boto3
from botocore.exceptions import ClientError
import json

secret_name = "Secret_name"
region_name = "region_name"

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name,
)


try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        print("The requested secret " + secret_name + " was not found")
    elif e.response['Error']['Code'] == 'InvalidRequestException':
        print("The request was invalid due to:", e)
    elif e.response['Error']['Code'] == 'InvalidParameterException':
        print("The request had invalid params:", e)
    elif e.response['Error']['Code'] == 'DecryptionFailure':
        print("The requested secret can't be decrypted using the provided KMS key:", e)
    elif e.response['Error']['Code'] == 'InternalServiceError':
        print("An error occurred on service side:", e)
else:
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']

    else:
        secret = get_secret_value_response['SecretBinary']

SOME_TOKEN = json.loads(secret)['SOME_TOKEN']




