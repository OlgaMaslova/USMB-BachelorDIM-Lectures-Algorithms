##
#
# @author : Olga Maslova, Licence DIM, IUT Annecy le Vieux, FRANCE
# @brief : a set of generic functions for data management

"""
# a variable
a=1 # default type : int

# an empty list
mylist=[]

#a filled list
mylist2=[1,2,3]

#append to a list
mylist.append(10)

#a buggy list
mybuggylist=[1, 'a', "Hi"]

#operators
b=a+2
mylist_sum=mylist+mylist2
"""

def average_above_zero(input_list):

    #init critical variable
    positive_values_sum=0
    positive_values_count=0
    
    first_item=input_list[0]
    
    #compute the average of positive elements of a list
    for item in input_list:
        #select only positive items    
        if item>0:
            positive_values_sum+=item
            positive_values_count+=1
        elif item==0:
            print('This value is null:'+str(item))
        else:
            print('This value is negative:'+str(item))     
    #compute the final average
    average=float(positive_values_sum)/float(positive_values_count)
    print('Positive elements average is '+str(average))
    return float(average)
"""    
#testing average_above_zero function:
mylist=[1,2,3,4,-7]
result= average_above_zero(mylist)
print(str(result))
message='The average of positive items of {list_value) is {res}'.format(list_value=mylist,res=result)
print(message)
"""
    
def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list: th einput list to be scanned
    # @throws an exception (ValueError) on an empty list
    
    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    
    #init max_value and its index
    max_value=input_list[0]
    max_idx=0
    
       
    #generic style : iterate over the range of list indexes
    for idx in range(len(input_list)):
        if max_value<input_list[idx]:
            max_value=input_list[idx]
            max_idx=idx      
            
    #modern style : iterate over indexes and members of the list 
    for idx, item  in enumerate(input_list):
        if max_value<item:
            max_value=item
            max_idx=idx
            
    return max_value, max_idx
"""   
#testing max_value function:
mylist=[1,2,3,4,-7]
mymax_tuple= max_value(mylist)
mymax=mymax_tuple[0]
print('The maximlum value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
"""


##
#Reverse a table (my Way)
def reverse_table(input_list):
    #Start from maximum index    
    index_max=len(input_list)
    for idx, item in enumerate(input_list):
        if index_max > idx:   
            index_max-=1
            input_list[idx]=input_list[index_max]
            input_list[index_max]=item
   
"""
#Reverse a table : another way
def reverse_table(input_list):
    lastidx=len(input_list)
    for idx in range(len(input_list)/2):
        lastidx-=1
        popped=input_list[idx]
        input_list[idx]=input_list[lastidx]
        input_list[lastidx]=popped
    
"""
    
"""    
#testing reverse_table
import copy
mylist=[1,5,4,-7]
listsave=copy.deepcopy(mylist)
reverse_table(mylist)
print(savelist)
print('The reversed list is {newlist}'.format(newlist=mylist))
"""

##
#Bounding Box

import numpy
import time
init_time=time.time()

size_rows=10
size_cols=10
myMat=numpy.zeros([size_rows,size_cols], dtype=int)
#set a value in a specific cell
myMat[1,3]=1    


#filling something in the matrix
"""for  row in range(5,8):
    for col in range(7,9):
        myMat[row,col]=1

"""

#filling the matrix: better way
myMat[2:4,5:9]=1
myMat[2:4,5:9]=numpy.ones([2,4])
print(myMat)

#output coordinates matrix
bbox_coords=numpy.zeros([4,2],dtype=int)
a=size_rows-1
c=0
b=size_cols-1
d=0
#check every element of myMat 
for row in range(0,size_rows-1):
    for col in range(0,size_cols-1):
        item = myMat[row,col]
        #if the element is 1, save its index(i,j)
        if item==1:
            if row<a:
                a=row
            elif row>c:
                c=row
            if col<b:
                b=col
            elif col>d:
                d=col      
#populate the coordinates matrix with the values
bbox_coords[0]=[a,b]  
bbox_coords[1]=[a,d] 
bbox_coords[2]=[c,b] 
bbox_coords[3]=[c,d] 
finish_time=time.time()
alltime=finish_time-init_time
print(bbox_coords)     
print(alltime)  
            
    
    
    
        






