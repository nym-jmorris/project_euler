'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n!/(n-r)!r!, where r <= n.

It is not until n=23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr for 1<=n<=100, are greater than one-million?

'''
from math import factorial

def choose(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

mils =0
limit = 1000000
for n in range(1,101):
    for r in range(1,n):
        if choose(n,r)>limit:
            mils += 1
print('There are {} combinations greater than {}'.format(mils,limit))