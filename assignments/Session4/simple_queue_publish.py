# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:47:06 2017

@author: maslovao
"""

import pika, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-concurrency', help='an integer for the accumulator', action = "store_true")
concurrency = parser.parse_args().concurrency

# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) #connect to CloudAMQP
channel = connection.channel() # start a channel
# Declare a durable queue
channel.queue_declare(queue='presentation', durable=True)
if concurrency:
    print("conc here!")
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