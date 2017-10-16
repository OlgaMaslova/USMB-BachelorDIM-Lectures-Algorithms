# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:41:07 2017

@author: maslovao
"""

# publish.py
#import simple_queue_publish.py
import subprocess, pika, os, argparse

def publishMsg():
    for i in range(0,3):
        string = 'py -2 simple_queue_publish.py -concurrency'
        subprocess.call(string, shell=True)
        i = i+1
        
def prepareTwoReaders():
    for i in range(0,2):
        string = 'py -2 simple_queue_read.py -concurrency'
        subprocess.call(string, shell=True)
        i = i+1        
        
        
prepareTwoReaders()        
publishMsg()

