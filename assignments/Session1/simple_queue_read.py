# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:50:21 2017

@author: maslovao
"""

import pika, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-concurrency', help='an integer for the accumulator', action = "store_true")
concurrency = parser.parse_args().concurrency
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='presentation')
#channel.basic_qos(prefetch_count=1)
countMsg = 0 

def callback(ch, method, properties, body):
  global countMsg 
  countMsg = countMsg + 1
  print(" [x] Received %r" % body)
  print("Total messages received", countMsg)
  if concurrency:
      print(" [x] Message processed, acknowledging (to delete message from the queue)")
      ch.basic_ack(delivery_tag = method.delivery_tag)
  
channel.basic_consume(callback,
                      queue='presentation',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press Ctrl+C')
channel.start_consuming()

