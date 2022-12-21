import boto3
import csv
from aws_connection import make_session, switch_session
import credentials.credentials as credentials


# csv_ob = open("inventory_info.csv", "w", newline='')
# csv_w = csv.writer(csv_ob)
# csv_w.writerow(['S_NO', "Instance_Id", 'Instance_Type', 'Architecture', 'LaunchTime', 'Privat_Ip'])

# make console session with assuming role for gathering rds instances on each account
for account, role in credentials.accounts.items():
    print(f'This is {account}.')
    
    assume_role = make_session(role)
    switch_role_sess = switch_session(assume_role)

    ec2_rs = switch_role_sess.resource(service_name='ec2', region_name='us-east-1')
    cnt = 1
	
    # for instance in all_instances:
    #     print(instance)
    f_ebs_unused = {'Name': 'status', 'Values': ['available']}

    for instance in ec2_rs.instances.all():
        print(account, cnt, instance.instance_id, instance.instance_type, \
            instance.architecture, instance.launch_time.strftime("%Y-%m-%d"), \
            instance.private_ip_address)
        # csv_w.writerow([cnt,instance.instance_id,instance.instance_type,instance.architecture,instance.launch_time.strftime("%Y-%m-%d"),instance.private_ip_address])

        cnt+=1

# csv_ob.close()
