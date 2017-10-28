#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:07:46 2017

@author: olgamaslova
"""

import pytest
import S3_imgproc_tools as img
import numpy as np

def test_invert_colors_manual_checkType():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.invert_colors_manual(myImg)
        
def test_invert_colors_manual_checkSize():
    myImg = np.zeros(2)
    with pytest.raises (ValueError):
        img.invert_colors_manual(myImg)
        
def test_invert_colors_numpy_checkType():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.invert_colors_numpy(myImg)
        
def test_invert_colors_opencv_checkType():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.invert_colors_opencv(myImg)
        
def test_threshold_image_manual_checkType():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.threshold_image_manual(myImg)
        
def test_threshold_image_manual_checkSize():
    myImg = np.zeros(2)
    with pytest.raises (ValueError):
        img.threshold_image_manual(myImg)
        
def test_threshold_image_numpy_checkType():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.threshold_image_numpy(myImg)
        
def test_threshold_image_opencv_checkType():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.threshold_image_opencv(myImg)