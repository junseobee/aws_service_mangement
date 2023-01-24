from aws_connection import make_session, switch_session
import credentials.credentials as credentials


for account, role in credentials.accounts.items():
    print(f'AWS Account: {account}')
    
    assume_role = make_session(role)
    switch_role_sess = switch_session(assume_role)

    health_client = switch_role_sess.client(service_name='health', region_name='us-east-1')
    ht_paginator = health_client.get_paginator('describe_events')
    response_iterator = ht_paginator.paginate()

    cnt = 0
    for items in response_iterator:
        for item in items['events']:
            if item['statusCode'] != 'closed':
                cnt += 1
                print('\t', str(cnt), item['statusCode'], item['service'], item['eventTypeCode'], \
                    item['eventTypeCategory'], item['startTime'], item['lastUpdatedTime'])
    