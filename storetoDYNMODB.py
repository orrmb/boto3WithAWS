import boto3


#Some data to store in Dynamo
prediction_summary = {
                    'prediction_id': '22',
                    'original_img_path': 555,
                    'predicted_img_path': 555,
                    'labels': {
                'class': 'dany' ,
                'cx': 'yoni',
                'cy': 'sahny',
                'width': 'sdadsa',
                'height': 'dasdsa',
            },
                    'time': str(213.23)
}


print(type(prediction_summary))



client = boto3.resource('dynamodb')
response = client.Table('Table_name')
response.put_item(Item=prediction_summary)










