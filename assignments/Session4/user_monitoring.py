#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:13:45 2017

@author: olgamaslova
"""

import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)  #connect to CloudAMQ
channel = connection.channel()  # start a channel
 # Declare a direct exchange
channel.exchange_declare(exchange='caramail',
                         exchange_type='direct')

#Create anonymous queue to bind it to the exchange
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

#Create binding to 'presentation' route:
channel.queue_bind(exchange='caramail',
                       queue=queue_name,
                       routing_key='presentation')

#number of Users
user_count = 0
#user's unique names
all_id = []

def callback(ch, method, props, body):
    global user_count
    #check if users has already logged in
    if body in all_id:
        print('user is already logged in')
    else:
        #register a new user
        user_count = user_count + 1
        all_id.append(body)
        print('%s users are logged in'% user_count)

channel.basic_consume(callback, queue=queue_name)
print(" [x] Awaiting for users")
channel.start_consuming()
