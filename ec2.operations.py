# Import all the modules and Libraries
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
response = ec2_console.stop_instances(
    InstanceIds=['i-04cxxxxxxxxf']
)

print(response)
# to set region -aws configure set region ap-south-1
# to check region -aws configure get region
