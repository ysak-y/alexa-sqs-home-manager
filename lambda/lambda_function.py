import boto3
from ask import alexa

client = boto3.client('sqs', region_name='us-east-1')

response = client.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/180047737375/test',
        MessageBody='foo'
        )

print(response)

