'''
#Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?
'''

from math import floor
import time

time0 = time.time()
nmax = 1000000

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


time1 = time.time()
for i in range(2,nmax):
    if candidates[i] == True:
        primes.append(i)
        updateSieve(i)

time2 = time.time()
print('Primes generated')

# rotate primes
# check for rotation in list of primes...

def hasEven(candidate):
    if str(candidate).find(0)>0:
        return True
    if str(candidate).find(2)>0:
        return True
    if str(candidate).find(4)>0:
        return True
    if str(candidate).find(6)>0:
        return True
    if str(candidate).find(8)>0:
        return True
    else return False

def checkPrime(candidate):
    if candidate in primes:
        return True
    else: return False

def rotatePrime(prime,i):
    pstr = str(prime)
    pr = pstr[-len(pstr)+i:]+pstr[0:i]
    return int(pr)

#test = 456

#print(rotatePrime(456,1))
cprimes = []

time3 = time.time()

for prime in primes:
    loops = 0
    primetest = []
    # the "in" is too slow...
    print('Testing {}...'.format(prime))
    while loops < len(str(prime)):
        testing = rotatePrime(prime,loops)
        if testing%2 == 0 and prime > 2:
            loops = len(str(prime))
            continue
        if testing%25 == 0:
            loops = len(str(prime))
            continue
        # this is the slow part...
        if testing in primes: 
            isPrime = 1 
        else: 
            loops = len(str(prime))
            continue
        primetest.append(isPrime)
        loops +=1
    if sum(primetest) == len(str(prime)):
        cprimes.append(prime)

time4 = time.time()
print(cprimes)
print('There are {} circular primes below 1 million.'.format(len(cprimes)))
print('Time 1: {} \nTime 2: {}\nTime 3: {}\nTime 4:{}'.format(time1-time0,time2-time0,time3-time0,time4-time0))
