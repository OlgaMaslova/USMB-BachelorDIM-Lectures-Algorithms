# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:32:44 2017

@author: maslovao
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
channel.queue_declare(queue='rpc_queue')  # Declare a queue

def on_request(ch, method, props, body): #process and reply function
        request_param = str(body) #retrieve input parameters
        decoded_message = msgpack.unpackb(request_param, object_hook=m.decode) #decode the message
        response = S3_imgproc_tools.invert_colors_opencv(decoded_message) #invert the image
        print(response.shape)
        encoded_response = msgpack.packb(response, default=m.encode)
        ch.basic_publish(exchange='', #reply
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
                                correlation_id = props.correlation_id),
                             	body=encoded_response)
        ch.basic_ack(delivery_tag = method.delivery_tag) #acknowledge
        
        
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()