#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:49:25 2017

@author: olgamaslova
"""

import pika, os, argparse, uuid
parser = argparse.ArgumentParser()
parser.add_argument("-signin", action="store_true")
signin = parser.parse_args().signin

# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)  #connect to CloudAMQ
channel = connection.channel()  # start a channel
 # Declare a direct exchange
channel.exchange_declare(exchange='caramail',
                         exchange_type='direct')

#unique correlation id
corr_id = str(uuid.uuid4())
message = 'Hello everyone!'
if signin:
    print('Logging in')
    channel.basic_publish(exchange='caramail',
                    routing_key='presentation',
                    body=corr_id)  #we pass unique id in message
else:
    print('Posting')
    channel.basic_publish(exchange='caramail',
                    routing_key='posts',
                    body=message) 


#creating subscribers
    
#Create anonymous queue 
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

#Create binding to 'posts' route:
channel.queue_bind(exchange='caramail',
                       queue=queue_name,
                       routing_key='posts')


def callback(ch, method, props, body):
    
    print('User from %s queue posted %s'%(queue_name,body))

channel.basic_consume(callback, queue=queue_name)
print(" [x] Awaiting for posts")
channel.start_consuming()