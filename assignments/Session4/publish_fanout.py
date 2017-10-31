#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:52:21 2017

@author: olgamaslova
"""

import pika, os, time

# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
#params.socket_timeout = 5
connection = pika.BlockingConnection(params) #connect to CloudAMQP
channel = connection.channel() # start a channel

# Declare a fanout echange
channel.exchange_declare(exchange='messages',
                         exchange_type='fanout')
message = 'Hello, how are you?'

#regulary emits messages every 5 seconds (if there are no subscribers, messages are lost)
for i in range(0,9):
    channel.basic_publish(exchange='messages',
                          routing_key='',
                          body=message)
    print(" [x] Sent %r" % message)
    time.sleep(5)
    i=i+1
    


connection.close()