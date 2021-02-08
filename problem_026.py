'''
#problem 26

# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1 

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
from math import floor

d = 1000
d = 10

# floating point math will ruin the party.
# here's 1/3: 0.33333333333333331482962

digits= [0 for iter in range(d)]
#print(digits)

def decimalize(num,denom):
    i = 0
    while num < denom:
        num = num * 10
        i+=1
    dvnd = int(floor(num/denom))
    rmdr = num%denom

    return i,dvnd,rmdr