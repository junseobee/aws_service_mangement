from aws_connection import make_session, switch_session
import credentials.credentials as credentials
import datetime


role = credentials.accounts['avon_shrd']

assume_role = make_session(role)
switch_role_sess = switch_session(assume_role)


iam_rs = switch_role_sess.resource(service_name='iam')


''' when calling a single user informaion
iam_user_obj = iam_rs.User('jason.noh@megazone.com')
# print(dir(iam_user_obj))
print(iam_user_obj.user_name, iam_user_obj.create_date.strftime('%Y-%m-%d %H:%M:%S'))
'''

# collect multiple users
user_iterator = iam_rs.users.all()

for user in user_iterator:
    print(user)

groups = group_iterator = iam_rs.groups.all()

for group in groups:
    print(group)