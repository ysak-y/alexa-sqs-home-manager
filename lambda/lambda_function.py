# -*- coding: utf-8 -*-
import boto3
from ask import alexa

def lambda_handler(request_obj, context=None):
    metadata = {}
    return alexa.route_request(request_obj, context)

@alexa.default_handler()
def default_handler(request):
    return alexa.respond('home manager')

@alexa.request_handler('LaunchRequest')
def launch_request_handler(request):
    return alexa.create_response(message='hello')

@alexa.request_handler('SessionEndedRequest')
def session_ended_request_handler(request):
    return alexa.create_response(message='GoodBye')

@alexa.request_handler('YeelightOn')
def yeelight_on_request_hander(request):
    client = boto3.client('sqs', region_name='us-east-1')

    response = client.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/180047737375/test',
            MessageBody='SwitchYeelight',
            MessageAttributes={
                'StringValue': 'On',
                'DataType': 'String'
                }
            )

    print(response)
    return alexa.create_response(message='yeelight on')

@alexa.request_handler('YeelightOff')
def yeelight_on_request_hander(request):
    client = boto3.client('sqs', region_name='us-east-1')

    response = client.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/180047737375/test',
            MessageBody='SwitchYeelight',
            MessageAttributes={
                'StringValue': 'Off',
                'DataType': 'String'
                }
            )

    print(response)
    return alexa.create_response(message='yeelight off')
