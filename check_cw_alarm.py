from aws_connection import make_session, switch_session
import credentials.credentials as credentials


for account, role in credentials.accounts.items():
    print(f'AWS Account: {account}')
    
    assume_role = make_session(role)
    switch_role_sess = switch_session(assume_role)

    cw_client = switch_role_sess.client(service_name='cloudwatch', region_name='us-east-1')
    cw_paginator = cw_client.get_paginator('describe_alarms')
    response_iterator = cw_paginator.paginate()

    cnt = 0
    for alarms in response_iterator:
        for alarm in alarms['MetricAlarms']:
            # if alarm['StateValue'] == 'INSUFFICIENT_DATA':
            if alarm['StateValue'] == 'ALARM':
            # if len(alarm['AlarmActions']) == 0: # to find alarms with no action
                if 'CPU-ASG-' not in alarm['AlarmName']:
                    cnt += 1
                    
                    print('\t', str(cnt), alarm['AlarmName'], alarm['StateValue'], alarm['MetricName'], \
                        alarm['Dimensions'][0]['Value'])
    