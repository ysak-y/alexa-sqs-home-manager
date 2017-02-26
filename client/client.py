# -*- coding: utf-8 -*-
import os
import time
import boto3
from yeelight import Bulb, discover_bulbs

ip = discover_bulbs()[0]['ip']
bulb = Bulb(ip)

def execute(body, attr):
    if body == 'SwitchYeelight':
        state = attr['switch']
        if state == 'on':
            try:
                bulb.turn_on()
            except ConnectionRefusedError:
                ip = discover_bulbs()[0]['ip']
                bulb = Bulb(ip)
                bulb.turn_on()
        else:
            try:
                bulb.turn_off()
            except ConnectionRefusedError:
                ip = discover_bulbs()[0]['ip']
                bulb = Bulb(ip)
                bulb.turn_off()

def inquire_new_message():
    client = boto3.client('sqs', region_name='us-east-1')
    
    response = client.receive_message(
            QueueUrl=os.environ['SQS_URL'],
            MessageAttributeNames=['All']
            )
    print(response)

    if 'Messages' in response.keys():
        message = response['Messages'][0]
        body = message['Body']
        attr = message['MessageAttributes']
        execute(body, attr)


if __name__ == '__main__':
    while True:
        time.sleep(2)
        inquire_new_message()
