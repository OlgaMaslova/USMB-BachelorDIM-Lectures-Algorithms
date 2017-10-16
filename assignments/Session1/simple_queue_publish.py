# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:47:06 2017

@author: maslovao
"""

import pika, os, sys

# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) #connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='presentation') # Declare a queue
if sys.argv == "-concurrency":
        channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='maslovao',
                      properties = pika.BasicProperties(delivery_mode = 2 #make message persistent
                      ))
else: 
    channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='maslovao')
print(" [x] Sent 'maslovao'!")
connection.close()