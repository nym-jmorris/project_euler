'''

Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''
# research here
# https://www.mathblog.dk/project-euler-70-investigate-values-of-n-for-which-%CF%86n-is-a-permutation-of-n/
# need the final number to be the product of two large-ish primes.

# Thinking here is
# 1.  Low ratios result from having as few factors as possible
# 2.  We should have a large n
#
# from the web:
# The obvious best choice would be to find a prime number close to 10.000.000. 
# However, that is not possible since a prime must end in 1,3,7,9 and φ(n) = n-1 would only change the last digit. 
# So they cannot be permutations of each other.
#
# To that end, we should look at numbers with two factors
# SQRT(10000000) ~~ 3250, so look at primes between 2000 and 5000.


from time import time

def isPerm(number1, number2):
    str1 = sorted(str(number1))
    str2 = sorted(str(number2))
    if str1 == str2:
        return True
    else: return False

#  Find all primes below the ceiling via Sieve of Eratosthenes:
ceiling = 10000000
nmax = 5000

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
t1 = time()

# don't need this
'''
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

def isPrime(n):
    p = 2
    if n<2:
        return False
    while p * p <= n:
        if n%p==0:
            return False
        p+=1
    return True    

def makephi(n):
    y = n
    for i in range(2,n+1):
        if isPrime(i) and n % i == 0:
            y *= 1 - 1.0/i
    return int(y)
'''

maxtot =0
maxi = 0

cprimes = []

for p in primes:
    if p>2000 and p<5000:
        cprimes.append(p)

bestratio = 100
bestnum = 0

for c1 in range(0,len(cprimes)):
    for c2 in range(c1+1,len(cprimes)):
        n = cprimes[c1]*cprimes[c2]
        if n > ceiling:
            break
        phi = (cprimes[c1]-1)*(cprimes[c2]-1)
        if n/phi < bestratio and isPerm(n,phi):
            bestratio = n/phi
            bestnum = n
print('Best ratio is for {}, with ratio {}'.format(bestnum,bestratio))
