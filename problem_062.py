'''

The cube, 41063625 (345**3), can be permuted to produce two other cubes: 
    56623104 (384**3)
    66430125 (405**3). 

In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
# https://www.geeksforgeeks.org/perfect-cube/
# Python3 program to check if a number
# is a perfect cube using prime factors
import math
 
# Inserts the prime factor in HashMap
# if not present
# if present updates it's frequency
def insertPF(primeFact, fact) :
 
    if (fact in primeFact) :
        primeFact[fact] += 1
    else :
        primeFact[fact] = 1
    return primeFact
   
# A utility function to find all
# prime factors of a given number N
def primeFactors (n) :
 
    primeFact = {}
   
    # Insert the number of 2s
    # that divide n
    while (n % 2 == 0) :
        primeFact = insertPF(primeFact, 2)
        n = n // 2
   
    # n must be odd at this point
    # So we can skip one element
    for i in range(3, int(math.sqrt(n)) + 1, 2) :
   
        # while i divides n, insert
        # i and divide n
        while (n % i == 0) :
            primeFact = insertPF(primeFact, i)
            n = n // i
   
    # This condition is to handle 
    # the case when n is a prime
    # number greater than 2
    if (n > 2) :
        primeFact = insertPF(primeFact, n)
    return primeFact
   
# Function to check if a 
# number is perfect cube
def isCube (n) :
 
    primeFact = {}
    primeFact = primeFactors(n)
   
    # Iteration in Map
    for x in primeFact :
        if (primeFact[x] % 3 != 0) :
            return False      
    return True

# https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
# Python3 code to convert tuple 
# into string
import functools
import operator 
  
def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str
  
#print(isCube(41063625))

from itertools import permutations

for i in range(345,350):
    num = i ** 3
    nperm = permutations(str(num))
    print('Here!')
    for p in nperm:
        ip = convertTuple(p)
        print(ip)
        if isCube(ip):
            print('{} has the following cubic permutation: {}'.format(num,ip))