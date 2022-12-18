from aws_connection import make_session, switch_session
import credentials.credentials as credentials


# make console session with assuming role for gathering rds instances on each account
for account, role in credentials.accounts.items():
    print(f'This is {account}.')
    
    assume_role = make_session(role)
    switch_role_sess = switch_session(assume_role)

    response = switch_role_sess.client(service_name='rds', region_name='us-east-1')
    db_instances = response.describe_db_instances()['DBInstances']
    
    if len(db_instances) > 0:
        print(f'\t{len(db_instances)} intance(s).')
        for instance in db_instances:
            # these outputs can be stored in a database permanently
            # need to grab some values for managing service
            print(f"instance: {instance['DBInstanceIdentifier']} engine: {instance['Engine']} status: {instance['DBInstanceStatus']} backup retention: {instance['BackupRetentionPeriod']} monitoring interval: {instance['MonitoringInterval']} performance insight: {instance['PerformanceInsightsEnabled']} del protection: {instance['DeletionProtection']}")
    else:
        print('\tno instance')
    
    print('-'*80)


# assume_role = make_session(credentials.accounts['avon_npci'])
# print(assume_role.get_caller_identity())

# switch_role_sess = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
#                       aws_secret_access_key=response['Credentials']['SecretAccessKey'],
#                       aws_session_token=response['Credentials']['SessionToken'])

# switch_role_sess = switch_session(assume_role)
# print(switch_role_sess.get_caller_identity())

# response = switch_role_sess.client(service_name='rds', region_name='us-east-1')

# print(response.describe_db_instance_automated_backups())
# for db in response.describe_db_instances()['DBInstances']:
#     print(db['DBInstanceIdentifier'])
#     print('-'*80)

# print(response.describe_db_instances()['DBInstances'])

# for instance in response.describe_db_instances()['DBInstances']:
#     print(instance['DBInstanceIdentifier'])

# for event in response.describe_events()['Events']:
#     print(event['SourceIdentifier'], event['Message'])
#     print('-'*80)
# df = pd.DataFrame.from_dict(response.describe_db_instances())

# print(df.info())
# print(df)