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
message='The average of positive items of {list_valu}) is {res}'.format(list_value=mylist,res=result)
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
    
    #init max_value
    max_value=input_list[0]
    
    #find the maximum value in the list
    for item in input_list:
        if max_value<item:
            max_value=item
    return max_value
 """   
#testing max_value function:
mylist=[1,2,3,4,-7]
result= max_value(mylist)
print('The maximlum value is: '+str(result))
"""

