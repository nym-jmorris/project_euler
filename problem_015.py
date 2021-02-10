'''

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

'''
from math import factorial

# Each move is either right or down
# limited to n moves of each

# rewrite to:
# how many 2n digit binary numbers with n ones are there...
# 2nCn

# 2n!/((2n-n)!n!)

size = 20

num = factorial(2*size)
denom = factorial(2*size - size)*factorial(size)

print(int(num/denom))