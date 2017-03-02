# -*- coding: utf-8 -*-
import os
import time
import boto3
from yeelight import Bulb, discover_bulbs
from multiprocessing import Process

ip = discover_bulbs()[0]['ip']
bulb = Bulb(ip)

def execute(body, attr):
    if body == 'SwitchYeelight':
        state = attr['switch']['StringValue']
        if state == 'On':
            response = bulb.turn_on()
        else:
            response = bulb.turn_off()

def inquire_new_message():
    client = boto3.client('sqs', region_name='us-east-1')
    
    response = client.receive_message(
            QueueUrl=os.environ['SQS_URL'],
            MessageAttributeNames=['All']
            )

    if 'Messages' in response.keys():
        message = response['Messages'][0]
        body = message['Body']
        attr = message['MessageAttributes']

        # Delete received message.
        receipt_handle = message['ReceiptHandle']
        response = client.delete_message(
                QueueUrl=os.environ['SQS_URL'],
                ReceiptHandle=receipt_handle
                )

        execute(body, attr)

def polling():
    while True:
        time.sleep(2)
        inquire_new_message()

if __name__ == '__main__':
    p = Process(target=polling)
    p.start()
