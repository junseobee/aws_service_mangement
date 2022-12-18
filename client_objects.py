import boto3

session = boto3.session.Session(profile_name='mzcread')

print(session)
iam_con_cli = session.client(service_name='iam', region_name='us-east-1')
ec2_con_cli = session.client(service_name='ec2', region_name='us-east-1')
s3_con_cli = session.client(service_name='s3', region_name='us-east-1')

# List all iam users using client object
response = iam_con_cli.list_users()
for each in response['Users']:
    print(each['UserName'])

# List all ec2 instance ids
# res_ec2 = ec2_con_cli.describe_instances()
# for each in res_ec2['Reservations']:
#     for each_instance in each['Instances']:
#         print(each_instance['InstanceId'])
#     print('-'*80)

# paginator = ec2_con_cli.get_paginator('describe_instances')
# print(paginator.paginate())
# for each in paginator.paginate():
#     print(each['Instances'])

# List all s3 buckets
# response = s3_con_cli.list_buckets()
# for each in response['Buckets']:
#     print(each['Name'])