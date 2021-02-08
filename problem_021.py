'''#problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
'''
from math import sqrt
from math import floor

def getFactors(n):
    factors =[]
    for i in range(1,floor(sqrt(n))+1):
        if n%i ==0:
            factors.append(i)
            factors.append(int(n/i))
    factors = list(dict.fromkeys(factors))
    factors.sort()
    factors.pop(len(factors)-1)
    return factors

def dn(factors):
    return sum(factors)

amicable =[]

for i in range(2,10000):
    f = getFactors(i)
    fsum = dn(f)
    #print('{}: d(n) = {} | {}'.format(i,fsum,f))

    if fsum == 1:
        continue
    if i == dn(getFactors(fsum)) and i != fsum:
        amicable.append(i)


for a in amicable:
    gf = getFactors(a)
    dngf = dn(gf)
    print('dn({:4d})=   {:4d} | Factors: {}'.format(a,dngf,gf))
    
print(sum(amicable))