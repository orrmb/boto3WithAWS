import json
import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SQS_URL'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=5,
)

for message in response.get("Messages", []):
    message = response['Messages'][0]['Body']
    print(message)



queue_name='sqs-aws-project'
sqs_client = boto3.client('sqs', region_name='us-west-2')
while True:
    response = sqs_client.receive_message(QueueUrl=queue_name, MaxNumberOfMessages=1, WaitTimeSeconds=5)

    if 'Messages' in response:
        print(response)
        message = response['Messages'][0]['Body']
        receipt_handle = response['Messages'][0]['ReceiptHandle']

        # Use the ReceiptHandle as a prediction UUID
        Some_value = response['Messages'][0]['MessageId']



