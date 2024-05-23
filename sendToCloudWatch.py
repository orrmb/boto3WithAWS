import boto3

backlog_per_instance=2

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Put custom metrics
cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'Metric_name',
            'Unit': 'None',
            'Value': 'Some_value'
        },
    ],
    Namespace='Some_namespace'
)
