#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:09:18 2017

@author: olgamaslova
"""

import pika, os
import numpy as np
import msgpack 
import msgpack_numpy as m
import cv2
import imp
 # puts the /foo directory at the start of your path
S3_imgproc_tools = imp.load_source('S3_imgproc_tools', '../Session1/S3_imgproc_tools.py')


# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)  #connect to CloudAMQ
channel = connection.channel()  # start a channel
# Declare a direct exchange
channel.exchange_declare(exchange='direct_images',
                         exchange_type='direct')
#Create anonymous queue to bind it to the exchange
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

#Create bindings according to the filter type:
filter_types = {'invert':'invert image colors', 'threshold':'threshold an image'}
for value in filter_types.itervalues():
    print(value)
    print(queue_name)
    channel.queue_bind(exchange='direct_images',
                       queue=queue_name,
                       routing_key=value)

def on_request(ch, method, props, body): #process and reply function
        decoded_message = msgpack.unpackb(body, object_hook=m.decode) #decode the message
        if method.routing_key == filter_types['invert']:
            response = S3_imgproc_tools.invert_colors_opencv(decoded_message) #invert the image
        else:
            response = S3_imgproc_tools.threshold_image_opencv(decoded_message) #treshold the image
        #encoding the processed image
        encoded_response = msgpack.packb(response, default=m.encode)
        #reply
        ch.basic_publish(exchange='', 
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
                                correlation_id = props.correlation_id),
                             	body=encoded_response)
        ch.basic_ack(delivery_tag = method.delivery_tag) #acknowledge
        
        
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue=queue_name)

print(" [x] Awaiting RPC requests")
channel.start_consuming()