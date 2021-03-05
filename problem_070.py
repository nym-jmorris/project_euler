'''

Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''

from time import time

t1 = time()

def isPerm(number1, number2):
    str1 = sorted(str(number1))
    str2 = sorted(str(number2))
    if str1 == str2:
        return True
    else: return False

#  Find all primes below the ceiling via Sieve of Eratosthenes:
ceiling = 1000000
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

for i in range(2,nmax):
    if candidates[i] == True:
        primes.append(i)
        updateSieve(i)    

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

maxtot =0
maxi = 0

for n in range(2,10):
    factors = factorize(n)
    f_count = {f:factors.count(f) for f in factors}
    phi = 1
    for k in f_count.keys():
        phi = phi * (k ** (f_count[k]-1)) * (k-1)
    print('n = {}, φ(n) = {}'.format(n,phi))

#    print('n = {}. {} has {} factors. They are {}. φ(n) = {}'.format(n,n,len(factors),factors,phi))
