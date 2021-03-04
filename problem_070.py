'''

Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''

from time import time

def isPerm(number1, number2):
    str1 = sorted(str(number1))
    str2 = sorted(str(number2))
    if str1 == str2:
        return True
    else: return False

# Find the prime factors of an integer:
def factorize(n):
    factors = []
    i = 0
    p = primes[i]
    while p <= n:
        while n % p == 0:
            factors.append(p)
            n = n // p
        if n == 1:
            break
        i += 1
        p = primes[i]
    return factors

ceiling = 10000

#  Find all primes below the ceiling via Sieve of Eratosthenes:
nmax = ceiling

primes = []

candidates = [True for iter in range(nmax)]

def updateSieve(prime):
    for i in range(0,nmax // prime):
        candidates[i*prime] = False
        try:
            candidates[i*prime+prime] = False
        except IndexError:
            None       
    return

for n in range(2,ceiling):

    factors = factorize(n)
    f_count = {f:factors.count(i) for f in factors}
    phi = 1
    for k in f_count.keys():
        phi = phi * k ** (f_count[k]-1) * (k-1)
    phi = phi * n

    tot = n / phi
    if tot > maxtot:
        maxtot = tot
        maxi = n

    if n % (ceiling // 10) == 0:
        progress = progress + 0.1
        print('{:7,d} integers ({:3.2%}) factorized and totiented in {:.2f} seconds'.format(n,progress,time()-t1))
        print('{} returns the highest totient so far, {:.2f}.'.format(maxi,maxtot))

print('{:7,d} integers ({:3.2%}) factorized and totiented in {:.2f} seconds'.format(nmax,1,time()-t1))

print('{} returns the highest totient, {:2f}.'.format(maxi,maxtot))