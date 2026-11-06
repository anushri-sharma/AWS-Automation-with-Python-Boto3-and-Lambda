Let's configure Boto3 on your MacBook using PyCharm, step by step. Since you're practising AWS IAM and EC2 automation, we'll configure your AWS credentials, region and Python environment properly.

# Step 1: Install Boto3

Open your PyCharm terminal.

Activate your project virtual environment if it isn't already active, then run:

```
pip install boto3
```

Verify installation:

```
pip show boto3
```

You should see the installed Boto3 version.

# Step 2: Configure AWS CLI

Boto3 uses AWS credentials configured through the AWS CLI.

First, check whether AWS CLI is installed:

```
aws --version
```

If it isn't installed, install it on your Mac using Homebrew:

```
brew install awscli
```

Now configure your AWS credentials:

```
aws configure
```

It will ask for four details:

| Prompt                | What to enter              |
| --------------------- | -------------------------- |
| AWS Access Key ID     | Your IAM access key ID     |
| AWS Secret Access Key | Your IAM secret access key |
| Default region name   | `ap-south-1`               |
| Default output format | `json`                     |

Security reminder

Create access keys for an IAM identity with only the permissions you need. Never share your secret access key or upload it to GitHub.

# Step 3: Check your AWS configuration

Run:

```
aws configure list
```

Expected configuration:

```
      Name                    Value
      ----                    -----
   profile                  <not set>
access_key              ****************XXXX
secret_key              ****************XXXX
    region                  ap-south-1
```

Your credentials are stored locally in:

```
~/.aws/credentials
```

Your configuration is stored in:

```
~/.aws/config
```

The default profile is automatically used when you don't specify another profile.

# Step 4: Verify your AWS identity

Run:

```
aws sts get-caller-identity
```

Expected output:

```
{
    "UserId": "AIDAEXAMPLE",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/example"
}
```

This confirms which AWS identity your credentials represent.

# Step 5: Connect Boto3 with AWS

Create a Python file in PyCharm:

`boto3_connection.py`

Use this code:

```
import boto3# Create AWS sessionaws_management_console = boto3.session.Session(    profile_name="default",    region_name="ap-south-1")# Print AWS regionprint("AWS Region:", aws_management_console.region_name)# Open STS clientsts_console = aws_management_console.client("sts")# Verify AWS identityresponse = sts_console.get_caller_identity()print("AWS Account:", response["Account"])print("AWS User ID:", response["UserId"])print("AWS ARN:", response["Arn"])print("Boto3 configured successfully!")
```

Run:

```
python boto3_connection.py
```

If successful, you'll see your AWS account and identity information.

# Step 6: Understand Boto3 configuration

There are three important concepts:

| Component | Purpose                                               |
| --------- | ----------------------------------------------------- |
| Session   | Manages AWS credentials and region                    |
| Client    | Connects to an AWS service                            |
| Resource  | Provides an object-oriented interface to AWS services |

Example:

```
import boto3# Sessionsession = boto3.Session(    profile_name="default",    region_name="ap-south-1")# Clientec2_client = session.client("ec2")# Resourceec2_resource = session.resource("ec2")# List instancesresponse = ec2_client.describe_instances()print(response)
```

# Step 7: Important AWS CLI commands

Keep these commands handy while learning Boto3.

| Command                       | Purpose               |
| ----------------------------- | --------------------- |
| `aws configure`               | Configure credentials |
| `aws configure list`          | View configuration    |
| `aws configure list-profiles` | View profiles         |
| `aws sts get-caller-identity` | Verify AWS identity   |
| `aws configure get region`    | Check default region  |
| `aws s3 ls`                   | List S3 buckets       |
| `aws ec2 describe-instances`  | List EC2 instances    |

# Step 8: Your Boto3 learning checklist

Configuration progress

# 0%

Install Boto3 in PyCharm

Install and verify AWS CLI

Configure AWS credentials

Set region to ap-south-1

Verify identity using STS

Connect to EC2 using Boto3

List IAM users using Boto3

[List- IAM Users](https://github.com/anushri-sharma/AWS-Automation-with-Python-Boto3-and-Lambda/blob/main/iam_list_users.py)
[List- Instances and check with instance id](https://github.com/anushri-sharma/AWS-Automation-with-Python-Boto3-and-Lambda/blob/main/list_ec2_instances.py)
Launch and stop a test EC2 instance

[launch](https://github.com/anushri-sharma/AWS-Automation-with-Python-Boto3-and-Lambda/blob/main/launch_ec2.py)

[Stop Instances/ Start/ Terminate](https://github.com/anushri-sharma/AWS-Automation-with-Python-Boto3-and-Lambda/blob/main/ec2.operations.py)
