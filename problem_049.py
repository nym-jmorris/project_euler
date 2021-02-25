'''

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
    (i) each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''


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


def isPerm(number1, number2):
    str1 = sorted(str(number1))
    str2 = sorted(str(number2))
    if str1 == str2:
        return True
    else: return False



p4=[]
for p in primes:
    if len(str(p))<4:
        continue
    p4.append(p)

#max gap would be front/middle/end of the set of primes.
maxgap = int((p4[len(p4)-1]-p4[0])/2)

gap = 2

while gap<maxgap:
    for p in p4:
        if isPrime(p + gap) and isPerm(p,p+gap) and isPrime(p+2*gap) and isPerm(p,p+2*gap):
            print('{}, {}, {} satisfy the conditions with a gap of {}. Terms concatenate to {}'.format(p,p+gap,p+2*gap,gap,str(p)+str(p+gap)+str(p+2*gap)))
        else: continue
    gap += 2