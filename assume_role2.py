import boto3
import credentials.credentials as credentials

mzcread_sess = boto3.session.Session(profile_name="mzcread")

# arn_pci = 'arn:aws:iam::594604260993:role/pci-viewonly'
# arn_qde = 'arn:aws:iam::984259802673:role/qde-viewonly'
# arn_npci = 'arn:aws:iam::151100372060:role/npci-viewonly'
# arn_shrd = 'arn:aws:iam::524593013124:role/shared-viewonly'
# arn_dmz = 'arn:aws:iam::881758745010:role/network-viewonly'
# arn_log = 'arn:aws:iam::851453209151:role/log-viewonly'

sts = mzcread_sess.client("sts")
response = sts.assume_role(
    RoleArn=credentials.avon_qde['arn'],
    RoleSessionName=credentials.avon_qde['name']
)
# print(response)
new_session = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                      aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                      aws_session_token=response['Credentials']['SessionToken'])
s3 = new_session.client("s3")
for bucket in s3.list_buckets()['Buckets']:
    print(bucket['Name'])

ec2 = new_session.client(service_name='ec2', region_name='us-east-1')
for each in ec2.describe_instances()['Reservations']:
    print('-'*80)
    for instance in each['Instances']:
        print(instance['InstanceId'])