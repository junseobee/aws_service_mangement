from aws_connection import make_session, switch_session
import credentials.credentials as credentials
import re


avon_qde_params = ['/ecom/springboot_qa/3rd.solution.salesforce.credentials.email.customer-bu.account-id',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.email.customer-bu.client-id',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.email.customer-bu.client-secret',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.email.rep-bu.account-id',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.email.rep-bu.client-id',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.email.rep-bu.client-secret',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.sms.customer-bu.account-id',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.sms.customer-bu.client-id',
                    '/ecom/springboot_qa/3rd.solution.salesforce.credentials.sms.customer-bu.client-secret',
                    '/ecom/springboot_qa/common.cloud.aws.credentials.access-key',
                    '/ecom/springboot_qa/common.cloud.aws.credentials.secret-key',
                    '/ecom/springboot_qa/common.security.sha.secret-key',
                    '/ecom/springboot_qa/spring.batch.datasource.password',
                    '/ecom/springboot_qa/spring.batch.datasource.username',
                    '/ecom/springboot_qa/spring.datasource.password',
                    '/ecom/springboot_qa/spring.datasource.username',
                    '/ecom/springboot_qa/spring.mq.datasource.password',
                    '/ecom/springboot_qa/spring.mq.datasource.username']

localqa_params = ['/ecom/springboot_localqa/3rd.solution.salesforce.credentials.email.customer-bu.account-id',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.email.customer-bu.client-id',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.email.customer-bu.client-secret',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.email.rep-bu.account-id',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.email.rep-bu.client-id',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.email.rep-bu.client-secret',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.sms.customer-bu.account-id',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.sms.customer-bu.client-id',
'/ecom/springboot_localqa/3rd.solution.salesforce.credentials.sms.customer-bu.client-secret',
'/ecom/springboot_localqa/common.cloud.aws.credentials.access-key',
'/ecom/springboot_localqa/common.cloud.aws.credentials.secret-key',
'/ecom/springboot_localqa/common.security.sha.secret-key',
'/ecom/springboot_localqa/spring.batch.datasource.password',
'/ecom/springboot_localqa/spring.batch.datasource.username',
'/ecom/springboot_localqa/spring.datasource.password',
'/ecom/springboot_localqa/spring.datasource.username',
'/ecom/springboot_localqa/spring.mq.datasource.password',
'/ecom/springboot_localqa/spring.mq.datasource.username']

localqa_cyber_params = ['/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.email.customer-bu.account-id',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.email.customer-bu.client-id',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.email.customer-bu.client-secret',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.email.rep-bu.account-id',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.email.rep-bu.client-id',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.email.rep-bu.client-secret',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.sms.customer-bu.account-id',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.sms.customer-bu.client-id',
'/ecom/springboot_localqa-cybersource/3rd.solution.salesforce.credentials.sms.customer-bu.client-secret',
'/ecom/springboot_localqa-cybersource/common.cloud.aws.credentials.access-key',
'/ecom/springboot_localqa-cybersource/common.cloud.aws.credentials.secret-key',
'/ecom/springboot_localqa-cybersource/common.security.sha.secret-key',
'/ecom/springboot_localqa-cybersource/spring.batch.datasource.password',
'/ecom/springboot_localqa-cybersource/spring.batch.datasource.username',
'/ecom/springboot_localqa-cybersource/spring.datasource.password',
'/ecom/springboot_localqa-cybersource/spring.datasource.username',
'/ecom/springboot_localqa-cybersource/spring.mq.datasource.password',
'/ecom/springboot_localqa-cybersource/spring.mq.datasource.username']

avon_shrd_params = ['/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.email.customer-bu.account-id',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.email.customer-bu.client-id',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.email.customer-bu.client-secret',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.email.rep-bu.account-id',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.email.rep-bu.client-id',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.email.rep-bu.client-secret',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.sms.customer-bu.account-id',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.sms.customer-bu.client-id',
'/ecom/springboot_local-cybersource/3rd.solution.salesforce.credentials.sms.customer-bu.client-secret',
'/ecom/springboot_local-cybersource/common.cloud.aws.credentials.access-key',
'/ecom/springboot_local-cybersource/common.cloud.aws.credentials.secret-key',
'/ecom/springboot_local-cybersource/common.security.sha.secret-key',
'/ecom/springboot_local-cybersource/spring.batch.datasource.password',
'/ecom/springboot_local-cybersource/spring.batch.datasource.username',
'/ecom/springboot_local-cybersource/spring.datasource.password',
'/ecom/springboot_local-cybersource/spring.datasource.username',
'/ecom/springboot_local-cybersource/spring.mq.datasource.password',
'/ecom/springboot_local-cybersource/spring.mq.datasource.username']


source_store = []

def sw_role(account):
    assume_role = make_session(account)
    switch_role_sess = switch_session(assume_role)

    client = switch_role_sess.client(service_name='ssm', region_name='us-east-1')

    return client

try:
    client = sw_role(credentials.accounts['avon_qde'])
        
    for para in avon_qde_params:
        response = client.get_parameter(Name=para, WithDecryption=True)['Parameter']
        # print(response)
        source_store.append(response)

    client = sw_role(credentials.accounts['avon_shrd'])

    for para in avon_shrd_params:
        response = client.get_parameter(Name=para, WithDecryption=True)['Parameter']
        # print(response)
        source_store.append(response)

    print(f'source_store size: {len(source_store)}')
except:
    print('Not found')



# aws ssm put-parameter --name "/TEST/PARA" --value "test" --type "String" --tier "Standard"

for para in source_store:
    name = re.sub('qa|local', 'localqa', para['Name'])
    print('aws ssm put-parameter --name "{0}" --value "{1}" --type "{2}" --tier "Standard"'.format(name, para['Value'], para['Type']))
