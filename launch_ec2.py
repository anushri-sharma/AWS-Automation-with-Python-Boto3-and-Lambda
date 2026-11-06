import boto3
from pprint import pprint


aws_management_console = boto3.session.Session(
    #to check profile name run aws configure list-profiles or aws configure list
    profile_name="default",
    region_name="ap-south-1"
)

ec2_console = aws_management_console.client("ec2")

response = ec2_console.run_instances(
    ImageId="ami-0cxxxxxxxxxx",
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1
)

pprint(response)
