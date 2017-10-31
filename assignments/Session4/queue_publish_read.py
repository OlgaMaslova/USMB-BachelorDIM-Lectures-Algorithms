# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:54:22 2017

@author: maslovao
"""

import argparse, pika, os

#switch between publish and read modes
parser = argparse.ArgumentParser()
parser.add_argument("-read", action="store_true", help = "help me!")
parser.add_argument("-publish", action="store_true")
args = parser.parse_args()
if args.read:
    print ('read turned on')
    execfile('simple_queue_read.py')
if args.publish:
    print ('publish turned on')
    execfile('simple_queue_publish.py')
    
    

    
