# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 11:32:12 2017

@author: maslovao
"""

import cv2
import numpy as np
import time

#read an image
img_gray = cv2.imread('myimage_4K.jpg',0)
image_bgr = cv2.imread('myimage_small.jpg',1)
image_medium = cv2.imread('myimage_medium.jpg', 1)
image_4K = cv2.imread('myimage_4K.jpg', 1)

#print("Gray levels image shape = "+str(img_gray.shape)) 

#cv2.imshow("Gray levels image", img_gray)
#cv2.waitKey()


##Reverse colors manually 
# @params input_img: ndarray
# @throws an exception (ValueError) on bad type of an input image, an exception (ValueError) on a not 3-layers image
def invert_colors_manual(input_img):
    #first check if provided image is a ndarray
    if str(type(input_img)) != '<type \'numpy.ndarray\'>':
        raise ValueError('provided image is not a ndarray!')
    #check if the image is an rgb image
    if len(input_img.shape) != 3:
        raise ValueError('provided image is not an rgb image')    
    start = time.time()
    img_inv = np.zeros(input_img.shape, dtype = np.uint8)
    for row_idx in xrange(input_img.shape[0]):
        for col_idx in xrange(input_img.shape[1]):
            for ch_idx in range(input_img.shape[2]):             
                img_inv[row_idx,col_idx,ch_idx] = 255-input_img[row_idx,col_idx,ch_idx]
    
    end = time.time()
    print(end - start)
    return img_inv

##Reverse colors using numpy 
# @params input_img: ndarray
# @throws an exception (ValueError) on bad type of an input image
def invert_colors_numpy(input_img):     
    #first check if provided image is a ndarray
    if str(type(input_img)) != '<type \'numpy.ndarray\'>':
        raise ValueError('provided image is not a ndarray!')
    start = time.time()
    img_inv =  255-input_img
    end = time.time()
    print(end - start)
    return img_inv

##Reverse colors using OpenCV library 
# @params input_img: ndarray
# @throws an exception (ValueError) on bad type of an input image
def invert_colors_opencv(input_img):   
    #first check if provided image is a ndarray
    if str(type(input_img)) != '<type \'numpy.ndarray\'>':
        raise ValueError('provided image is not a ndarray!')
    start = time.time()
    img_inv =  cv2.bitwise_not(input_img)
    end = time.time()
    print(end - start)
    return img_inv 

##Image thresholding manually
# @params input_img: ndarray 
# @throws an exception (ValueError) on bad type of an input image, an exception (ValueError) on a not 3-layers image 
    
# Set threshold and max_value
thresh = 100
max_value = 255
def threshold_image_manual(input_img): 
    #first check if provided image is a ndarray
    if str(type(input_img)) != '<type \'numpy.ndarray\'>':
        raise ValueError('provided image is not a ndarray!')
        #check if the image is an rgb image
    if len(input_img.shape) != 3:
        raise ValueError('provided image is not an rgb image (3 layers)')   
    start = time.time()
    img_inv = np.zeros(input_img.shape, dtype = np.uint8)
    for row_idx in xrange(input_img.shape[0]):
        for col_idx in xrange(input_img.shape[1]): 
            for ch_idx in range(input_img.shape[2]):    
                if input_img[row_idx,col_idx,ch_idx] > thresh:
                    img_inv[row_idx,col_idx,ch_idx] = max_value
                else:
                    img_inv[row_idx,col_idx,ch_idx] = 0    
    end = time.time()
    print(end - start)
    return img_inv

##Image thresholding using numpy 
# @params input_img: ndarray
# @throws an exception (ValueError) on bad type of an input image
def threshold_image_numpy(input_img):     
    #first check if provided image is a ndarray
    if str(type(input_img)) != '<type \'numpy.ndarray\'>':
        raise ValueError('provided image is not a ndarray!')
    start = time.time()
    img_zeros = np.zeros(input_img.shape, dtype = np.uint8)
    img_inv = np.where(input_img < thresh, img_zeros, max_value)
    end = time.time()
    print(end - start)
    return img_inv


##Image thresholding with OpenCV library using Otsu method
# @params input_img: ndarray, grayscale image
# @throws an exception (ValueError) on bad type of an input image 
def threshold_image_opencv(input_img):
    #first check if provided image is a ndarray
    if str(type(input_img)) != '<type \'numpy.ndarray\'>':
        raise ValueError('provided image is not a ndarray!')
    start = time.time()
    inv_tuple = cv2.threshold(input_img,0,max_value,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    end = time.time()
    print(end - start)
    return inv_tuple[1]


""" 
#testing functions
img_inv = invert_colors_manual(img_gray) 
img_numpy = invert_colors_numpy(image_bgr) 
img_openCV = invert_colors_opencv(image_bgr)
img_inv = threshold_image_opencv(img_gray) 

cv2.imshow("Inverted", img_inv)
cv2.waitKey()
"""            
   
  
    
   
    