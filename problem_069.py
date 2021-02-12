'''


Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

# generate primes
# build gcd

from math import gcd

ceiling = 1000000
ceiling = 1000

nmax = ceiling

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

maxtot = 0
maxi = 0

for i in range(2,ceiling+1):
    tot = i/phi(i)
    if tot > maxtot:
        maxtot = tot
        maxi = i

print('{} has the largest totient: {}'.format(maxi,maxtot))