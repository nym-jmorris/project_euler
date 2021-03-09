'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
'''

# let's see if patterns emerge from smaller batches...
# each increment in d adds phi(d) to the number of proper fractions
# can we compute phi(d) for 1MM numbers?
# compute the primes, phi(d) = d-1


''' Exploratory code below'''
# from math import gcd

# from time import time

# def hcf(n,d):
    
#     while True:
#         q = d//n
#         r = d-q*n
#         if r==0:
#             return n
#         d = n
#         n = r


# limit = 10
# for denom in range(2,limit+1):

#     t0 = time()
#     pfracs = []
#     cfracs = [] #cleaned
#     for d in range(2,denom+1):
#         for n in range(1,d):
#             if hcf(n,d) == 1:
#                 pfracs.append(str(n)+'/'+str(d))
#             elif hcf(int(n/gcd(n,d)),int(d/gcd(n,d))) == 1:
#                 pfracs.append(str(int(n/gcd(n,d)))+'/'+str(int(d/gcd(n,d))))
#             else: continue
#     t1 = time()
#     [cfracs.append(x) for x in pfracs if x not in cfracs] 
#     t2 = time()

#     #cfracs = pfracs.copy()
#     print('d = \t{}\tFractions: \t{}'.format(denom,len(cfracs)))

# from time import time

# def isPrime(n):
#     p = 2
#     if n<2:
#         return False
#     while p * p <= n:
#         if n%p==0:
#             return False
#         p+=1
#     return True

# def makephi(n):
#     y = n
#     for i in range(2,n+1):
#         if isPrime(i) and n % i == 0:
#             y *= 1 - 1.0/i
#     return int(y)

# #  Find all primes below the ceiling via Sieve of Eratosthenes:
# ceiling = 10000
# nmax = ceiling

# primes = []

# candidates = [True for iter in range(nmax)]

# def updateSieve(prime):
#     for i in range(0,nmax // prime):
#         candidates[i*prime] = False
#         try:
#             candidates[i*prime+prime] = False
#         except IndexError:
#             None       
#     return

# t0 = time()

# for i in range(2,nmax):
#     if candidates[i] == True:
#         primes.append(i)
#         updateSieve(i)

# t1 = time()

# fcount = 0

# for i in range(2,nmax):
#     # if isPrime(i):
#     #     fcount += i-1
#     # else: fcount += makephi(i)
#     fcount += makephi(i)


# https://www.mathblog.dk/project-euler-72-reduced-proper-fractions/

# In a sieve of Eratosthenes we make a list of all numbers up to the limit we are interested in.  
# We then start at the first prime and remove any multiple of that since any multiple will be 
# a composite number with the found prime as a factor. 
# We then move on to the next number which is not removed and remove any multiple of that. 
# We need to apply the same technique here. 
# However, instead of removing multiples of the primes we need to multiply them with 1-1/p  
# Doing that means we will eventually do that with all prime factors of every number.

from time import time

ceiling = 1000000
nmax = ceiling

phi = [i for i in range(0,nmax+1)]
result = 0
for i in range(2,ceiling+1):
    if phi[i] == i:
        for j in range(i,ceiling+1,i):
            phi[j] = int(phi[j] / i * (i-1))
    result += phi[i]

print(result)