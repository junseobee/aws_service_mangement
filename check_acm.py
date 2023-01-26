from aws_connection import make_session, switch_session
import credentials.credentials as credentials
from datetime import datetime, timedelta


for account, role in credentials.accounts.items():
    print(f'AWS Account: {account}')
    
    assume_role = make_session(role)
    switch_role_sess = switch_session(assume_role)

    acm_client = switch_role_sess.client(service_name='acm', region_name='us-east-1')
    acm_paginator = acm_client.get_paginator('list_certificates')
    response_iterator = acm_paginator.paginate()

    cnt = 0
    # print(datetime.today() + timedelta(days=30))
    for items in response_iterator:
        for item in items['CertificateSummaryList']:
            if item['InUse']:
                if item['NotAfter'].date() < (datetime.now() + timedelta(days=30)).date()w:
                    # print(item)
                    # print(str(item['InUse']))
                    print('\t', str(cnt), item['DomainName'], item['Status'], item['Type'], \
                        str(item['InUse']), item['NotAfter'].strftime('%d-%b-%Y (%H:%M)'))
                    cnt += 1
            # if item['statusCode'] == 'upcoming': # 'open'|'closed'|'upcoming'
            #     cnt += 1
            #     print('\t', str(cnt), item['statusCode'], item['service'], item['eventTypeCode'], \
            #         item['eventTypeCategory'], item['startTime'], item['lastUpdatedTime'])
    