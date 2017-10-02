# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 09:56:36 2017

@author: maslovao
"""

import pytest
import S1_algotools as algo
 

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