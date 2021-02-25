'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

ceiling = 1000000

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


def isPrime(n):
    p = 2
    if n<2:
        return False
    while p * p <= n:
        if n%p==0:
            return False
        p+=1
    return True

#primes_small = primes[0:25] #for testing the sub 100 chain...

# the chain 2+3+.. which busts the ceiling first is our upper limit for chainlength

ubound = 0
ulimit = 0
for p in primes:
    if ubound > nmax:
        break
    ubound += p
    ulimit = primes.index(p)

#only need to test inside the first ulimit primes...
primes_small = primes[0:ulimit+1] 

chainlength = ulimit

for ch in range(2,chainlength+1):
    for i in range(0,len(primes_small)-ch+1):
        psum = sum(primes_small[i:i+ch])
        if psum<nmax:
            if isPrime(psum):
                #print('Chainlength: {}\t{}\t{}'.format(ch,primes[i:i+ch],psum))
                print('Chainlength: {}\t{:,d}'.format(ch,psum))