import json

import boto3

sqs = boto3.client('sqs')

queue_url = 'SQS_URL'

#Some message
message = {'chat_id' : 7897 , 'img_name' : '12345', 'caption': 'blur'}
# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageBody=json.dumps(message)
)
print(response)