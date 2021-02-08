# problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# answer = 142913828922

import time
from math import floor

time_start = time.time()

nmax = 2000000

primes = []

candidates = [True for iter in range(nmax)]

def updateSieve(prime):
    for i in range(0,floor(nmax/prime)):
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
        if len(primes)%1000 == 0:
            print('\nPrime # {} found in {} seconds.'.format(len(primes),time.time()-time_start))
            print('Prime value: {}'.format(i))
            print('Prime density: {}'.format(len(primes)/i))

time_end = time.time()

print('There are {} primes below {}.'.format(len(primes),nmax))

print('\nFinished!')
print('Last prime before {} is: {}'.format(nmax,primes[len(primes)-1]))
print('Computation has taken {} seconds so far.'.format(time.time()-time_start))
print('Prime density: {}'.format(len(primes)/primes[len(primes)-1]))
print('The sum of the first {} primes is: {}\n'.format(len(primes),sum(primes)))
