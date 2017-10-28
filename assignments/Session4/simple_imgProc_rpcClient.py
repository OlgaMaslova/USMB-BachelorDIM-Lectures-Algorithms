# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:45:31 2017

@author: maslovao
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
channel.queue_declare(queue='rpc_queue')  # Declare a queue

result = channel.queue_declare(exclusive=True) #Client creates an anonymous exclusive callback queue
callback_queue = result.method.queue

image_medium = cv2.imread('myimage_medium.jpg', 1) #import an image
encoded_msg=msgpack.packb(image_medium, default=m.encode)
#print("length of encoded matrix: ", len(encoded_msg))

corr_id = str(uuid.uuid4())

channel.basic_publish(exchange='',
                    routing_key='rpc_queue',
                    properties=pika.BasicProperties(
                            reply_to = callback_queue,
                            correlation_id = corr_id,),
                            body=encoded_msg)                       
                           
response=None

def on_response(ch, method, props, body):
    if corr_id == props.correlation_id:
        global response
        decoded_response = msgpack.unpackb(str(body), object_hook=m.decode) #decode the response
        print(decoded_response.shape)
        cv2.imshow("Inverted", decoded_response)
        cv2.waitKey()
    else:
        raise ValueError("Correlation_id does not match!") #throxs an exception

print('Starting to wait on the response queue')
channel.basic_consume(on_response, no_ack=True,
                      queue=callback_queue)
while response is None: # wait for an answer
    connection.process_data_events()
connection.close()