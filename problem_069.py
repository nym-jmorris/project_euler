'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n = 6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

# generate primes
# factorize everything below the ceiling
# compute totients

ceiling = 1000000
ceiling = 1000000

from time import time

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

t0 = time()

for i in range(2,nmax):
    if candidates[i] == True:
        primes.append(i)
        updateSieve(i)
t1 = time()
print('{:7,d} primes found in {:.2f} seconds'.format(len(primes),time()-t0))

''' this code is unnecessary...

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


maxtot = 0
maxi = 0

# could make a hash table as we go:
# start with ceiling, 

# Iterate from 2 to the ceiling, computing the totient for each n
# Works fine, but is slow.  Factorization becomes unwieldy for large numbers.

# works fine. Factorization needs to be faster
# are the dictionary lookups slow too?

# closed form phi function using factors via wikipedia:
# https://en.wikipedia.org/wiki/Euler%27s_totient_function#Proof_of_Euler's_product_formula


# progress = 0.0
# for n in range(2,nmax):
#     factors = factorize(n)
#     f_count = {f:factors.count(i) for f in factors}
#     phi = 1
#     for k in f_count.keys():
#         phi = phi * k ** (f_count[k]-1) * (k-1)
#     phi = phi * n

#     tot = n / phi
#     if tot > maxtot:
#         maxtot = tot
#         maxi = n
# #    totients.append(tot)
#     if n % (ceiling // 10) == 0:
#         progress = progress + 0.1
#         print('{:7,d} integers ({:3.2%}) factorized and totiented in {:.2f} seconds'.format(n,progress,time()-t1))
#         print('{} returns the highest totient so far, {:.2f}.'.format(maxi,maxtot))

# print('{:7,d} integers ({:3.2%}) factorized and totiented in {:.2f} seconds'.format(nmax,1,time()-t1))

# print('{} returns the highest totient, {:2f}.'.format(maxi,maxtot))
'''

# largest totient will come from a number with a lot of small primes
# largest product of primes under 1MM is 2*3*5*7*11*13*17

product = 1
string = ''
factors = []
for p in range(0,len(primes)):
    if product * primes[p] < ceiling:
        product = product * primes[p]
        string = string+', ' +str(primes[p]) 
        factors.append(primes[p])
    else: break

phi = 1

for f in factors:
    phi = phi * (f-1)

print('{:,} has the highest totient under {:,}: {:.2f}'.format(product,nmax,product/phi))
print('It''s factors are {}'.format(string[2:]))
