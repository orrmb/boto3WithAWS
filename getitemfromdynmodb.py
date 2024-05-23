import boto3



client = boto3.client('dynamodb')

respone = client.get_item(Key={
    'prediction_id':{
        'S': 'Some_string'
    }
},
    TableName='Table_name'
)

print(respone)







