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
    
def test_average_above_zero_listNegative():  
    myList = [2, -1, -2]
    with pytest.raises (ValueError):
        algo.average_above_zero(myList)
        
def test_average_above_zero_listWithZero():  
    myList = [2, 1, 0]
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

def test_reverse_table_tableDifValues():
    myList = [1, 2.5, -7, 0]
    reversedList = list(reversed(myList))
    assert algo.reverse_table(myList) == reversedList
    
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
    
def test_roi_bbox_noOnesBox():
    myMat=numpy.zeros([6,6], dtype=int)
    with pytest.raises (ValueError):
        algo.roi_bbox(myMat)
        
def test_roi_bbox_EmptyBox():
    myMat = [] 
    with pytest.raises (ValueError):
         algo.roi_bbox(myMat)
         
def test_random_fill_sparse_MyMatCharWithKPositive():
    myMat = numpy.zeros((100,100), dtype=str)
    print(myMat.dtype)
    K = 10
    count = count_item_matrix(algo.random_fill_sparse(myMat, K))
    assert count == K
    
def count_item_matrix(myMat):
    
    item = "X"
    count = 0
    for i in range(len(myMat)):
        for j in range(len(myMat)):
            if item == myMat[i,j]:
                count+=1
    return count
   
def test_random_fill_sparse_MyMatNotChar():
    myMat = numpy.zeros([4,4], dtype=int)  
    K = 1
    with pytest.raises (ValueError):
         algo.random_fill_sparse(myMat, K)
         
def test_random_fill_sparse_MyMatEmpty():
    myMat = numpy.zeros([0,0], dtype=str)
    K=1
    with pytest.raises (ValueError):
         algo.random_fill_sparse(myMat, K)

def test_random_fill_sparse_KNegative():
    myMat = numpy.zeros((4,4), dtype=str)
    K = -1
    with pytest.raises (ValueError):
         algo.random_fill_sparse(myMat, K) 
         
def test_random_fill_sparse_KSuperiorThanSizeMyMat():
    myMat = numpy.zeros((4,4), dtype=str)
    K = 5
    with pytest.raises (ValueError):
         algo.random_fill_sparse(myMat, K) 
    
def test_remove_whitespace_normal():
    myString = 'my string'
    assert algo.remove_whitespace(myString) == 'mystring'
    
def test_remove_whitespace_onlySpaces():
    myString = '   '
    assert algo.remove_whitespace(myString) == ''
    
def test_shuffle_listIsEmpty():
    myList = []
    with pytest.raises (ValueError):
        algo.shuffle(myList)
     
def test_shuffle_sameMembersAndList():
     myList = ['a', 'J', 'B', 'v']
     newList = algo.shuffle(myList)    
     assert sorted(newList) == sorted(myList)  
     
def test_sort_Selective_normalScenario():
    myList = [1, 51.5, 25, -19]
    assert algo.sort_Selective(myList)[0] == sorted(myList)
    
def test_sort_Selective_emptyList():
    myList = []
    with pytest.raises (ValueError):
        algo.sort_Selective(myList)
        
def test_sort_bubble_normalScenario():
    myList = [0, 51.5, 25, -19]
    assert algo.sort_bubble(myList)[0] == sorted(myList)
    
def test_sort_bubble_emptyList():
    myList = []
    with pytest.raises (ValueError):
        algo.sort_bubble(myList)
    
    
