#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:40:26 2017

@author: olgamaslova
"""

import pika, uuid, os
import numpy as np
import msgpack 
import msgpack_numpy as m
import cv2


# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)  #connect to CloudAMQ
channel = connection.channel()  # start a channel
 # Declare a direct exchange
channel.exchange_declare(exchange='direct_images',
                         exchange_type='direct')

#Client creates an anonymous exclusive callback queue
result = channel.queue_declare(exclusive=True) 
callback_queue = result.method.queue

#import an image
my_image = cv2.imread('myimage_medium.jpg', 0) 
filter_types = {'invert':'invert image colors', 'threshold':'threshold an image'}
my_filter = filter_types['threshold']

#encodes the image
message = msgpack.packb(my_image, default=m.encode)
#unique correlation id
corr_id = str(uuid.uuid4())
print(my_filter)

channel.basic_publish(exchange='direct_images',
                    routing_key=my_filter,
                    properties=pika.BasicProperties(
                            reply_to = callback_queue,
                            correlation_id = corr_id,),
                            body=message)                                         
response=None

def on_response(ch, method, props, body):
    if corr_id == props.correlation_id:
        global response
        decoded_response = msgpack.unpackb(str(body), object_hook=m.decode) #decode the response
        print(decoded_response.shape)
        cv2.imshow("Inverted", decoded_response)
        cv2.waitKey()
    else:
        raise ValueError("Correlation_id does not match!") #throws an exception

print('Starting to wait on the response queue')
channel.basic_consume(on_response, no_ack=True,
                      queue=callback_queue)
while response is None: # wait for an answer
    connection.process_data_events()
connection.close()