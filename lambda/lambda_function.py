# -*- coding: utf-8 -*-
import boto3
from ask import alexa
import os

def lambda_handler(request_obj, context=None):
    metadata = {}
    return alexa.route_request(request_obj, context)

@alexa.default_handler()
def default_handler(request):
    return alexa.create_response(message='home manager', end_session=True)

@alexa.request_handler('LaunchRequest')
def launch_request_handler(request):
    return alexa.create_response(message='hello')

@alexa.request_handler('SessionEndedRequest')
def session_ended_request_handler(request):
    return alexa.create_response(message='GoodBye')

@alexa.intent_handler('YeelightOn')
def yeelight_on_request_hander(request):
    client = boto3.client('sqs', region_name='us-east-1')

    response = client.send_message(
            QueueUrl=os.environ['SQS_URL'],
            MessageBody='SwitchYeelight',
            MessageAttributes={
                'switch': {
                    'StringValue': 'On',
                    'DataType': 'String'
                    }
                }
            )

    print(response)
    return alexa.create_response(message='yeelight on', end_session=True)

@alexa.intent_handler('YeelightOff')
def yeelight_on_request_hander(request):
    client = boto3.client('sqs', region_name='us-east-1')

    response = client.send_message(
            QueueUrl=os.environ['SQS_URL'],
            MessageBody='SwitchYeelight',
            MessageAttributes={
                'switch': {
                    'StringValue': 'Off',
                    'DataType': 'String'
                    }
                }
            )

    print(response)
    return alexa.create_response(message='yeelight off', end_session=True)
