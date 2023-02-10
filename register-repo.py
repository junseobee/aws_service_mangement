import boto3
import requests
from requests_aws4auth import AWS4Auth
from aws_connection import make_session, switch_session
import credentials.credentials as credentials


avoqde = credentials.accounts['avon_qde']
assume_role = make_session(avoqde)
switch_role_sess = switch_session(assume_role)

host = 'https://vpc-avon-elasticsearch-qa-d7lyj3xyqdruk4i6iodxxv5xfi.us-east-1.es.amazonaws.com/'
region = 'us-east-1'
service = 'es'
credential = switch_role_sess.get_credentials()
# print(credential.access_key, credential.secret_key, region, service, credential.token)
awsauth = AWS4Auth(credential.access_key, credential.secret_key, region, service, session_token=credential.token)

# Register repository
path = '_snapshot/my-snapshot-repo' # the Elasticsearch API endpoint
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": "snapshots-for-opensearch",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::984259802673:role/ROL-Snapshot-Opensearch"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)