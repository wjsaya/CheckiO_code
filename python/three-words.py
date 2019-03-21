#!/bin/env/python
#coding: utf-8
#https://py.checkio.org/mission/three-words/solve/

#Let's teach the Robots to distinguish words and numbers.
#
#You are given a string with words and numbers separated by whitespaces (one space). 
#The words contains only letters. You should check if the string contains three words in succession. 
#For example, the string "start 5 one two three 7 end" contains three words in succession.
#
#Input: A string with words.
#
#Output: The answer as a boolean.
#
#Precondition: The input contains words and/or numbers. 
#There are no mixed words (letters and digits combined).
#0 < len(words) < 100 



def checkio(words):
    count = 0
    print (type(words))
    for i in words.split(' '):
        print (i,i.isalpha())
        if count < 3:
            if i.isalpha() == False:
                count = 0
            else:
                count += 1
    
    if count < 3:
        return False
    else:
        return True                                     

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print (checkio("one two 3 four five 6 seven eight 9 ten eleven 12 "))

    print (checkio("Hello World hello "))

    