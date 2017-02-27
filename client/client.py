# -*- coding: utf-8 -*-
import os
import time
import boto3
from yeelight import Bulb, discover_bulbs

ip = discover_bulbs()[0]['ip']
bulb = Bulb(ip)

print(ip)
print(bulb)

def execute(body, attr):
    if body == 'SwitchYeelight':
        state = attr['switch']['StringValue']
        if state == 'On':
            response = bulb.turn_on()
            print("%s is %s" % (bulb, response))
        else:
            response = bulb.turn_off()
            print("%s is %s" % (bulb, response))

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
        receipt_handle = message['ReceiptHandle']
        execute(body, attr)


if __name__ == '__main__':
    while True:
        time.sleep(2)
        inquire_new_message()
