import boto3


# make aws console session by view-only role using mzcread user
def make_session(role):
    mzcread_sess = boto3.session.Session(profile_name="mzcread")

    sts = mzcread_sess.client("sts")
    # response = switch_role(credentials.avon_qde)
    response = sts.assume_role(
        RoleArn=role['arn'],
        RoleSessionName=role['name']
    )

    return response


# switch role to access to other accounts
def switch_session(assume_role):
    switch_role_sess = boto3.Session(aws_access_key_id=assume_role['Credentials']['AccessKeyId'],
                      aws_secret_access_key=assume_role['Credentials']['SecretAccessKey'],
                      aws_session_token=assume_role['Credentials']['SessionToken'])
    
    return switch_role_sess