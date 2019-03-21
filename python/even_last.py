#!/usr/bin/env python
#https://py.checkio.org/mission/even-last/
#coding:utf-8

# You are given an array of integers. You should find
# the sum of the elements with even indexes (0th, 2nd, 4th...)
# then multiply this summed number and the final element of the array together.
# Don't forget that the first element has an index of 0.
#
#For an empty array, the result will always be 0 (zero).
#
#Input: A list of integers.
#
#Output: The number as an integer.
#
#Precondition: 0 ≤ len(array) ≤ 20
#all(isinstance(x, int) for x in array)
#all(-100 < x < 100 for x in array)
#所有数相加然后乘以最后一个


def checkio(array):
    if (len(array) <= 0):
        return 0
    if (len(array) > 20):
        return 0

    sum = 0
    for i in range(0,len(array)):
        if (i%2 == 0):
            sum += array[i]

    return (sum*array[-1])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    #assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    #assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    #assert checkio([6]) == 36, "(6)*6=36"
    #assert checkio([]) == 0, "An empty array = 0"
    #print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
   
    print (checkio([0,1,2,3,4,5]))
    #print (checkio([1, 3, 5]))
    #print (checkio([6]))
    #print (checkio([]))
