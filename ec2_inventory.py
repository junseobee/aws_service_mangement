import boto3
import csv
from aws_connection import make_session, switch_session
import credentials.credentials as credentials


csv_ob = open('.//output//inventory_info2.csv', 'w', newline='')
csv_w = csv.writer(csv_ob)
csv_w.writerow(['AWS_Account', "Instance_Id", 'Instance_Type', 'Architecture', \
    'Platform', 'LaunchTime', 'Privat_Ip', 'State', 'VPC_Id', 'Subnet_Id'])

# make console session with assuming role for gathering rds instances on each account
for account, role in credentials.accounts.items():
    print(f'This is {account}.')
    
    assume_role = make_session(role)
    switch_role_sess = switch_session(assume_role)

#     ec2_instances = switch_role_sess.describe_instances()['Reservations']
	
#     for instance in ec2_instances['Instances']:
#         print(account, cnt, instance['InstanceId'], instance['InstanceType'], instance['Platform'], \
#             instance['PrivateIpAddress'], 
#             )
    ec2_rs = switch_role_sess.resource(service_name='ec2', region_name='us-east-1')

    for instance in ec2_rs.instances.all():
        print(account, instance.instance_id, instance.instance_type, \
            instance.architecture, instance.platform, instance.launch_time.strftime("%Y-%m-%d"), \
            instance.private_ip_address, instance.state['Name'], instance.vpc_id, instance.subnet_id)
        csv_w.writerow([account, instance.instance_id, instance.instance_type, \
            instance.architecture, instance.platform, instance.launch_time.strftime("%Y-%m-%d"), \
            instance.private_ip_address, instance.state['Name'], instance.vpc_id, instance.subnet_id])


csv_ob.close()