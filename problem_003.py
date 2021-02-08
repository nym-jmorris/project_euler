'''



The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


'''

n = 600851475143
#n = 4101
#n = 13195 

factors =[]

from math import sqrt
from math import floor

for i in range(1,floor(sqrt(n))+1):
    if n%i == 0:
        factors.append(i)
        factors.append(int(n/i))
factors.sort()
factors.pop(len(factors)-1)
factors.pop(0)
print('Factors: {}'.format(factors))

dead_factors = []
pfactors = []

for f in range(len(factors)-1,-1,-1):
    for g in range(0,len(factors)):
        if int(factors[f])%int(factors[g])==0 and int(factors[f]) != int(factors[g]):
            if int(factors[f]) not in dead_factors:
                dead_factors.append(int(factors[f]))

dead_factors.sort()
print('Dead factors: {}'.format(dead_factors))

for f in factors:
#    print(f)
#    print('{} is in dead: {}.'.format(f,int(f) in dead_factors))

    if int(f) not in dead_factors:
        pfactors.append(int(f))
        
print('Prime Factors: {}'.format(pfactors))