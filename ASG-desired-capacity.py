import boto3

asg_client = boto3.client('autoscaling', region_name='region_name')

respone = asg_client.update_auto_scaling_group(AutoScalingGroupName='ASG_name',DesiredCapacity=1)
