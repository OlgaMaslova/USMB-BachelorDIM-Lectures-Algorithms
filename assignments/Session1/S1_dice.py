#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:57:26 2017

@author: olgamaslova
@brief: dice game
"""
import numpy

def shuffle(myList):

    for idx in range(len(myList)) :
        #generate a random index
        idx1 = alea(len(myList)-1)
        #initialize a helper item
        helperItem = myList[idx1]
        #swap two items of the list
        myList[idx1] = myList[idx]
        myList[idx] = helperItem        
    return myList
def alea(v):
    random = numpy.random.randint(1, v+1)
    return random
    
#initialize the variables
dice = [1,2,3,4,5,6]
userSum = 0
compSum = 0

#calculate the computer's turn
def computerTurn(compSum):
    #initialize temporary sum
    compSumTemp = compSum
    # Computer's turn
    print("Computer's turn")
    compNumber = alea(6)
    print("It got ", compNumber) 
    while compNumber != 1:
        compSumTemp = compSumTemp + compNumber
        #if compThrows = 2 it stops, if 1 it continues
        compThrows = alea(2) 
        #computer decides to continue
        if compThrows == 1:
            print("Computer decides to continue")
            compNumber = alea(6)
            print("It got ", compNumber) 
        #computer stops, validation of temporary sum
        else:
            print("Computer decides to stop")
            compSum = compSumTemp
            break
    return compSum
 
#interaction with a user 
def userTurn(dice):
    stringTurn = input("Roll the dice: choose a number from 1 to 6\n")
    dice = shuffle(dice)
    userNumber = dice[int(stringTurn)-1]
    print("You threw ", userNumber) 
    return userNumber

#find out if the user wants to continue his turn    
def userWantsToContinue(userNumber, userSum, dice):
    userSumTemp = userSum
    while userNumber != 1:
        userSumTemp = userSumTemp + userNumber
        userThrows = input(" Do you want to continue? y/n")
        print("Is the user throwing again?", userThrows)
        #user decides to continue
        if userThrows == "y": 
            userNumber = userTurn(dice)
        #user decides to stop
        else:
            userSum = userSumTemp
            break
    return userSum
        
    
#game starts user's turn first
userThrows = "y"

while userSum < 20 and compSum < 20: 
    if userThrows == "y":
        userNumber = userTurn(dice)
        userSum = userWantsToContinue(userNumber, userSum, dice)
        userThrows = "n"
        print("Your sum is so far ",userSum)
    else: 
        compSum = computerTurn(compSum)
        userThrows = "y"
        print("Computer's sum is so far ",compSum)  
        
#announce the winner        
if userSum  >= 20:
    print("You won!")
else:
    print("Computer won...")
        


    


    