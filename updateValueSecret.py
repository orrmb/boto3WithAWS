import boto3


secret_name = "secret-name"
region_name = "region"
profile_name="Profile-name"

session = boto3.Session(profile_name=profile_name, region_name=region_name)
secret_manager_client = session.client('secretsmanager')
respone = secret_manager_client.put_secret_value(SecretId='bootcamp-token',SecretString='{"token":"1234"}')
