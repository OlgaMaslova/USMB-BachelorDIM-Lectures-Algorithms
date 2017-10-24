# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 11:32:12 2017

@author: maslovao
"""

import cv2
import numpy as np
import time

#read an image
img_gray = cv2.imread('myimage_small.jpg',0)
image_bgr = cv2.imread('myimage_small.jpg',1)
image_medium = cv2.imread('myimage_medium.jpg', 1)
image_4K = cv2.imread('myimage_4K.jpg', 1)
print("Gray levels image shape = "+str(img_gray.shape)) 

#cv2.imshow("Gray levels image", img_gray)
#cv2.waitKey()

print(image_4K.shape)

def invert_colors_manual(input_img):
    start = time.time()
    img_inv = np.zeros(input_img.shape, dtype = np.uint8)
    for rowIdx in xrange(input_img.shape[0]):
        for colIdx in xrange(input_img.shape[1]):
            for chIdx in range(input_img.shape[2]):             
                img_inv[rowIdx,colIdx,chIdx] = 255-input_img[rowIdx,colIdx,chIdx]
    
    end = time.time()
    print(end - start)
    return img_inv
def invert_colors_numpy(input_img):     #inverion with numpy  
    start = time.time()
    img_inv =  255-input_img
    end = time.time()
    print(end - start)
    return img_inv
    
def invert_colors_opencv(input_img):   #inverion with openCV
    start = time.time()
    img_inv =  cv2.bitwise_not(input_img)
    end = time.time()
    print(end - start)
    return img_inv 
    
    
img_inv = invert_colors_manual(image_4K)
img_numpy = invert_colors_numpy(image_4K)
img_openCV = invert_colors_opencv(image_4K)

cv2.imshow("Inverted", img_numpy)
cv2.waitKey()
            
        
  
    
   
    