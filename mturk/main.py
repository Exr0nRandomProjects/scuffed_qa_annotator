import boto3

from creds import ACCESS_ID, ACCESS_KEY

client = boto3.client(
        'mturk',
        endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=ACCESS_KEY)

print(client.get_account_balance())

