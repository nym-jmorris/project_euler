'''

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

'''

# there must be a trick that reveals the bounds of this problem...
# forums say upper bound is 9999999 as 
#   9 999 999 is an easy upper limit to come up with. 7 times 9! is less than 9999999.


# The upper bound is 7 x 9!, because all 8-digit numbers (10,000,000 to 99,999,999) 
# are greater than the maximum possible result of any 8-digit number (f 99,999,999 = 2,903,040). 
#  [9! + 9! + 9! + 9! + 9! + 9! + 9!]

# 9! * 6 is greater than 6 digits...

# After 7 digits, there can be no more that are equal because the distance 
# between the minimum candidate and the maximum possible result (which is smaller) only increases.


from math import factorial

n = 145

for n in range(3,7*factorial(9)):
    sums = 0
    for i in range(0,len(str(n))):
        sums = sums + factorial(int(str(n)[i]))
        if sums == n:
            print('{} matches the criteria'.format(n))
