'''problem 6

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1+2+3+...+10)**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.
'''

sum_sqr = 0
sqr_sum = 0

for i in range(1,101):
    sum_sqr += i**2
    sqr_sum += i

sqr_sum = sqr_sum**2

print(sqr_sum - sum_sqr)