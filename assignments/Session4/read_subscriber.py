#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:58:01 2017

@author: olgamaslova
"""

import pika, os

# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
#params.socket_timeout = 5
connection = pika.BlockingConnection(params) #connect to CloudAMQP
channel = connection.channel() # start a channel
#declare an exchange
channel.exchange_declare(exchange='messages',
                         exchange_type='fanout')
# Create a random exclusive queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

#binding an exchange and the queue
channel.queue_bind(exchange='messages',
                   queue=queue_name)

print('Waiting for messages. To exit press CTRL+C')

#Callback on received message
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()