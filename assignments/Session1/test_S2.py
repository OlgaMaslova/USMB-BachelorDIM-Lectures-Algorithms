# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 09:56:36 2017

@author: maslovao
"""

import pytest
import S1_algotools as algo
import numpy
 

def test_average_above_zero_listAllPositive():
    myList = [1,2,3]
    assert algo.average_above_zero(myList) == 2 
    
def test_average_above_zero_listNegativeAndZero():  
    myList = [-1, -2, -3]
    with pytest.raises (ValueError):
        algo.average_above_zero(myList)

def test_max_value_listInt():
    myList = [0,-2,15]
    assert algo.max_value(myList) == (15, 2)
    
def test_max_value_listFloat():
    myList = [1.5, 2.15, -15.333]
    assert algo.max_value(myList) == (2.15,1)
    
def test_max_value_listEmpty():
    myList = []
    with pytest.raises (ValueError):
        algo.max_value(myList)

def test_reverse_table_tablePositiveAndZero():
    myList = [1, 2.5, 7, 19]
    assert algo.reverse_table(myList) == [19, 7, 2.5, 1]
    
def test_reverse_table_tableEmpty():
    myList = []
    with pytest.raises (ValueError):
        algo.reverse_table(myList)

def test_roi_bbox_smallSquarelBox():
    myMat=numpy.zeros([5,5], dtype=int)
    myMat[0:2,2:4]=1
    assert numpy.all(algo.roi_bbox(myMat) == [[0,2], [0,3], [1,2], [1,3]])
    
def test_roi_bbox_differentShapeBox():
    myMat=numpy.zeros([6,6], dtype=int)
    myMat[0:1,4:5]=1
    myMat[2:4,0:4]=numpy.ones([2,4])
    assert numpy.all(algo.roi_bbox(myMat) == [[0,2], [0,4], [3,2], [3,4]])
    
def test_roi_bbox_emptyBox():
    myMat=numpy.zeros([6,6], dtype=int)
    assert numpy.all(algo.roi_bbox(myMat) == [[0,0], [0,0], [0,0], [0,0]])