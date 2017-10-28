#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:07:46 2017

@author: olgamaslova
"""

import pytest
import S3_imgproc_tools as img
import numpy as np

def test_invert_colors_manual_checkArray():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.invert_colors_manual(myImg)
        
def test_invert_colors_manual_checkRGB():
    myImg = np.zeros(2)
    with pytest.raises (ValueError):
        img.invert_colors_manual(myImg)
        
def test_invert_colors_numpy_checkArray():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.invert_colors_numpy(myImg)
        
def test_invert_colors_opencv_checkArray():
    myImg = 'string'
    with pytest.raises (ValueError):
        img.invert_colors_opencv(myImg)
        
