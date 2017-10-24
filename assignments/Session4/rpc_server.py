# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:00:09 2017

@author: maslovao
"""

import pika, os

# Access the CLODUAMQP_URL environment variable and parse it 
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dilmpqbx:L7jYevAgl3H8swMcNA1lPd-fX3nqD3I1@lark.rmq.cloudamqp.com/dilmpqbx')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)  #connect to CloudAMQ
channel = connection.channel()  # start a channel
channel.queue_declare(queue='rpc_queue')  # Declare a queue


def on_request(ch, method, props, body): #process and reply function
        request_param = str(body)# retrieve input parameters
        print(request_param) #print the message
        response = 'Fine, and you?' #process the message
        ch.basic_publish(exchange='', #reply
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
correlation_id = props.correlation_id),
                         		body=str(response))
        ch.basic_ack(delivery_tag = method.delivery_tag) #acknowledge
        
        
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()

