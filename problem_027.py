'''
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 

However, when n = 40, 40^2 + 40 + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.

The product of the coefficients, −79 and 1601, is −126,479.

Considering quadratics of the form:

n^2 + an + b,  where |a| < 1,000 and |b| <= 1,000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''



# how do I bind n?  Let's see what brute force gets us...
# brute force yields a = -61, b = 971 for ab = -59231

# One solution in the forums has a function to test if prime
# is it faster than searching the giant list?  Hopefully?

'''
#ceiling = 200000

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

for i in range(2,nmax):
    if candidates[i] == True:
        primes.append(i)
        updateSieve(i)
'''

alimit = 1000
blimit = 1000

maxlen = 0 


# SUPER SLOW

# from time import time
# time0 = time()
# for a in range(-alimit+1,alimit):
#     if abs(a)%((alimit)//10)==0:
#         print('Starting {} loop for values of a'.format(a))
#     for b in range(-blimit,blimit+1):
#         # if abs(b)%((blimit)//5)==0:
#         #      print('Starting {} loop for values of b'.format(b))
#         nprimes = []
#         for n in range(0,max(abs(a),abs(b))):
#             result = n**2 + a*n + b
#             if result < 0:
#                 break
#             try:
#                 if primes.index(result) > 0:
#                     nprimes.append(result)
#             except ValueError:
#                 break
#         if len(nprimes)==0:
#             continue
#         if len(nprimes)<=maxlen:
#             continue
#         maxlen = len(nprimes)
#         print('New long chain found! {} and {} yield {} consective primes.  Coefficient product is {}.'.format(a,b,len(nprimes),a*b))
# timef = time()

# print('Computation took {} seconds.'.format(timef-time0))


def isPrime(n):
    p = 2
    if n<2:
        return False
    while p * p <= n:
        if n%p==0:
            return False
        p+=1
    return True

maxlen = 0
for a in range(-alimit+1,alimit):
    for b in range(-blimit,blimit+1):
        n = 0
        count = 0
        while True:
            if isPrime(n**2 + a*n + b):
                count+=1
                n+=1
            else: break
        if count>maxlen:
            maxlen = count
            print('{:4d}, {:4d} yield {:4d} consecutive primes. Coefficient product = {}'.format(a,b,count,a*b))

