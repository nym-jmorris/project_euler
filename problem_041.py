'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''
from math import floor
import time

time0 = time.time()

nmax = 999999999
nmax = 10000000

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
    if i%(nmax//10)==0:
        print('Through {:,} candidates'.format(i))
print('Through {:,} candidates'.format(nmax))

time2 = time.time()
print('{:,} primes generated in {:.2f} seconds'.format(len(primes),time2-time1))



def checkPand(prime):
    lenp = len(str(prime))
    for i in range(1,lenp+1):
        if str(i) not in str(prime):
            return False
    return True

pandps= []

for p in primes:
    if checkPand(p):
        pandps.append(p)

print('{} is the largest pandigital prime under {:,}.  It has {} digits '.format(max(pandps),nmax*100,len(str(max(pandps)))))

# Only need to test numbers up to seven digits in length.  From the forums:
    # Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
    # Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)


