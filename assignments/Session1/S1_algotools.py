#coding: utf-8
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
            raise ValueError('Zero value is not accepted')
        else:
            print('This value is negative:'+str(item)) 
            raise ValueError('Negative value is not accepted')
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
    # @param input_list: the input list to be scanned
    # @throws an exception (ValueError) on an empty list
    
    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    
    #init max_value and its index
    max_value=input_list[0]
    max_idx=0
    
    """  
    #generic style : iterate over the range of list indexes
    for idx in range(len(input_list)):
        if max_value<input_list[idx]:
            max_value=input_list[idx]
            max_idx=idx      
    """      
    #modern style : iterate over indexes and members of the list 
    for idx, item  in enumerate(input_list):
        if max_value<item:
            max_value=item
            max_idx=idx
            
    return max_value, max_idx
"""  
#testing max_value function:
mylist=[]
mymax_tuple= max_value(mylist)
mymax=mymax_tuple[0]
print('The maximlum value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
"""


##
#Reverse a table (my Way)
# @param input_list: the input list to be reversed
# @throws an exception (ValueError) on an empty list
def reverse_table(input_list):
    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #Start from maximum index    
    index_max=len(input_list)
    for idx, item in enumerate(input_list):
        if index_max > idx:   
            index_max-=1
            input_list[idx]=input_list[index_max]
            input_list[index_max]=item
    return input_list
   
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
print(listsave)
print('The reversed list is {newlist}'.format(newlist=mylist))
"""


import numpy
import time

##Bounding Box
# calculates the coordinates of the non-zero area in the 2D matrix
# @param my_mat: the input 2D matrix to be analyzed
# @throws an exception (ValueError) on an empty matrix, an exception (ValueError) if the matrix does not contain any ones to calculate

def roi_bbox(my_mat):
    #first check if the input matrix is of certain size
    if len(my_mat) == 0:
        raise ValueError("Your matrix is empty!")
   
    #output coordinates matrix
    bbox_coords=numpy.zeros([4,2],dtype=int)
    a=len(my_mat)
    c=0
    b=len(my_mat[0])
    d=0
    #check if there are ones to counter
    item = 1
    if item  in my_mat:
        print("You are ok, continue!")
    else: 
        raise ValueError("Fill in you matrix first!")
    
    #check every element of myMat 
    for row in range(0,a):
        for col in range(0,b):
            item = my_mat[row,col]
            #if the element is 1, save its index(i,j)
            if item==1:
                if row<a:
                    a=row
                elif row>c:
                    c=row
                if col<d:
                    b=col
                elif col>d:
                    d=col      
    #populate the coordinates matrix with the values
    bbox_coords[0]=[a,b]  
    bbox_coords[1]=[a,d] 
    bbox_coords[2]=[c,b] 
    bbox_coords[3]=[c,d] 
    
    return bbox_coords 
"""
##testing roi_bbox
size_rows=6
size_cols=6
myMat=numpy.zeros([size_rows,size_cols], dtype=int)
#filling the matrix: better way
myMat[0:1,4:5]=1
myMat[2:4,0:4]=numpy.ones([2,4])
print(myMat)
init_time=time.time()
result_coordinates=roi_bbox(myMat)
finish_time=time.time()
alltime=finish_time-init_time
print(result_coordinates)
"""
##Random filling of the matrix
# fill random K positions with 'X'
# @param my_mat: the input 2D matrix of type char, K: number of positions to fill  
# @throws an exception (ValueError) on an bad type matrix, an exception (ValueError) on an empty matrix, an exception (ValueError) on negative or superior to matrix's size value of K
def random_fill_sparse(my_mat,K):  
    #check if the input matrix is of type char
    if str(my_mat.dtype)[:2] != '|S' and str(my_mat.dtype)[:2] != '<U':
        print(my_mat.dtype)
        raise ValueError("Your matrix is not of type char!")
    #check if the input matrix is of certain size
    if len(my_mat) == 0:
        raise ValueError("Your matrix is empty!")
    #check if K is not negative or bigger than matrix's size
    if K < 0 or K > len(my_mat) :
        raise ValueError("Cannot fill negative nmber of cells or superior of the matrix's size!")
    #the size of the array       
    size_array=len(my_mat) 
    #init iteration 
    i = 0
    while i<K:
        #generate random row and column
        random_row = alea(size_array-1)
        random_col = alea(size_array-1)
        #print(random_row,random_col)
        #fill the cell with coordinates random_row and random_col with "X" if it is empty
        if my_mat[random_row,random_col] != "X":
            my_mat[random_row,random_col]="X"
            i+=1
    return my_mat
    
def alea(v):
    random = numpy.random.randint(0, v+1)
    return random
    
"""
##testing random_fill_sparse
N = 6  
myMat=numpy.zeros([N,N], dtype=str)
K=2
print(myMat)  
random_fill_sparse(myMat, K)
print(myMat)
"""

def remove_whitespace (myString):
    myString = myString.replace(' ','')
    return myString

"""
##testing remove_whitespace
myString = "azr gbn4b ok"
print(myString)
myString = remove_whitespace(myString)
print(myString)
"""
##
#Shuffle a list
def shuffle(myList):
    #check if the inputlist is not empty
    if len(myList) == 0:
        raise ValueError("Your list is empty!")
        
    for idx in range(len(myList)) :
                #generate a random index
                idx1 = alea(len(myList)-1)
                #initialize a helper item
                helperItem = myList[idx1]
                #swap two items of the list
                myList[idx1] = myList[idx]
                myList[idx] = helperItem 
                print(myList)
    return myList

   
##testing shuffle
myList = [3,5,6,7]
print (myList)
shuffle(myList)
print (myList)

 
## 
#Illustation of selective sorting (question (a))      
def sort_Selective(myList):
    #check if the inputlist is not empty
    if len(myList) == 0:
        raise ValueError("Your list is empty!")
    #itirations
    i=0
    #permutation
    p=0
    for idx in range(len(myList)):
        i+=1
        min_idx = idx
        for ind in range(idx+1, len(myList)):
            i+=1
            if myList[idx] > myList[ind]:
                min_idx = ind
                #swap two items of the list
                p+=1 
                myList[idx] , myList[min_idx] = myList[min_idx], myList[idx]
        #number of iterations does not depends on the content of the initial vector, but on its length (n) precisely (b)
        #(n²+n)/2 = 28 iterations (where n is the length of the list) needed to sort this list (c)
        #13 of permutations performed  it depends on the order of initial list (d), 
        #(n²+n)/2 = 28 comparisons applied (e)
        #the complexity is O(n²) 
    return myList, i, p
""" 
##testing sort_Selective
#myList = [10, 15, 7, 1, 3, 3, 9]
myList = []
for i in range(100):
    item = alea(100)
    myList.append(item)
shuffle(myList)
print(myList)
results_tuple = sort_Selective(myList)
print('Number of iterations is {i}, number of permutations is {p}'.format(i=results_tuple[1], p=results_tuple[2]))

# (g) for  n = 50, comparisons = 1275, permutaions : varied
#     for n = 100, comparisons = 5050, permutaions : varied
#     for n = 500, comparisons = 125250, permutaions : varied
"""

##
#Illustration of bubble sorting (a)
def sort_bubble(myList):
    #check if the inputlist is not empty
    if len(myList) == 0:
        raise ValueError("Your list is empty!")
    #itirations
    i = 0
    #permutation
    p = 0
    #comparison
    c = 0
    is_sorted = False
    #correction to reduce the length of the list for each outer loop
    m=0
    while is_sorted == False:
        i += 1 
        is_sorted = True
        for idx in range(len(myList)-1-m):
            i += 1
            c += 1
            if myList[idx]>myList[idx+1]:
                is_sorted = False
                #swap two items of the list
                p += 1
                myList[idx], myList[idx+1] = myList[idx+1], myList[idx]
            #print(myList, idx, i, c, p)
        m += 1 
        #number of iterations depends on the content of the initial vector, on its length (n) precisely (b)
        #28 iterations  needed to sort this list (c)
        #13 of permutations performed  it depends on the order of initial list (d), 
        #24 comparisons applied (e)
        #the complexity is O(n²) 
    return myList, i, p, c 

"""
##testing sort_bubble
#myList = [10, 15, 7, 1, 3, 3, 9]
myList = []
for i in range(100):
    item = alea(1000)
    myList.append(item)
shuffle(myList)
results_tuple = sort_bubble(myList)
print(results_tuple[3])
print('Number of iterations is {i}, number of permutations is {p}'.format(i=results_tuple[1], p=results_tuple[2]))

# (g) for  n = 50, comparisons varied, permutaions : varied, max is n*(n-1)/2= 1225
#     for n = 100, comparisons varied, permutaions : varied, max is n*(n-1)/2 = 4950
#     for n = 500, comparisons varied, permutaions : varied, max is n*(n-1)/2 = 124750
"""






