'''
problem 37

The number 3797 has an interesting property. 

Being prime itself, it is possible to continuously remove digits from 
left to right, and remain prime at each stage: 3797, 797, 97, and 7. 

Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from 
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


approach:

Build lists of 
    6 digit primes
    5 digit primes
    4 digit primes
    3 digit primes
    2 digit primes
    1 digit primes

define leftTrunc(p,digits)
define rightTrunc(p,digits)

for p in primes6:
    is leftTrunc(p,1) in primes(5)
    is rightTrunc(p,1) in primes(5)

    if leftTrunc(p,2) in primes(4)
    is rightTrunc(p,2) in primes(4)

    if leftTrunc(p,3) in primes(3)
    is rightTrunc(p,3) in primes(3)

    if leftTrunc(p,4) in primes(2)
    is rightTrunc(p,4) in primes(2)

    if leftTrunc(p,5) in primes(1)
    is rightTrunc(p,5) in primes(1)
'''

from math import floor 

nmax = 1000000
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

for i in range(2,nmax):
    if candidates[i] == True:
        primes.append(i)
        updateSieve(i)

def rightTrunc(prime,digits):
    return int(str(prime)[0:len(str(prime))-digits])

def leftTrunc(prime,digits):
    return int(str(prime)[digits:len(str(prime))])
    

#print(len(primes))

primes6=[]
primes5=[]
primes4=[]
primes3=[]
primes2=[]
primes1=[2,3,5,7]

for p in primes:
    if len(str(p))==6:
        primes6.append(p)
    if len(str(p))==5:
        primes5.append(p)
    if len(str(p))==4:
        primes4.append(p)
    if len(str(p))==3:
        primes3.append(p)
    if len(str(p))==2:
        primes2.append(p)

p_trunc =[]

for p in primes6:
    if rightTrunc(p,1) in primes5:
        if leftTrunc(p,1) in primes5:
            if rightTrunc(p,2) in primes4:
                if leftTrunc(p,2) in primes4:
                    if rightTrunc(p,3) in primes3:
                        if leftTrunc(p,3) in primes3:
                            if rightTrunc(p,4) in primes2:
                                if leftTrunc(p,4) in primes2:
                                    if rightTrunc(p,5) in primes1:
                                        if leftTrunc(p,5) in primes1:
                                            p_trunc.append(p)

for p in primes5:
    if rightTrunc(p,1) in primes4:
        if leftTrunc(p,1) in primes4:
            if rightTrunc(p,2) in primes3:
                if leftTrunc(p,2) in primes3:
                    if rightTrunc(p,3) in primes2:
                        if leftTrunc(p,3) in primes2:
                            if rightTrunc(p,4) in primes1:
                                if leftTrunc(p,4) in primes1:
                                    p_trunc.append(p)

for p in primes4:
    if rightTrunc(p,1) in primes3:
        if leftTrunc(p,1) in primes3:
            if rightTrunc(p,2) in primes2:
                if leftTrunc(p,2) in primes2:
                    if rightTrunc(p,3) in primes1:
                        if leftTrunc(p,3) in primes1:
                            p_trunc.append(p)

for p in primes3:
    if rightTrunc(p,1) in primes2:
        if leftTrunc(p,1) in primes2:
            if rightTrunc(p,2) in primes1:
                if leftTrunc(p,2) in primes1:
                    p_trunc.append(p)

for p in primes2:
    if rightTrunc(p,1) in primes1:
        if leftTrunc(p,1) in primes1:
            p_trunc.append(p)

print(p_trunc)

p_temp=p_trunc.copy()
p_temp.sort()
print(p_temp)
p_final=[]
for p in p_temp:
    if p in p_final:
        continue
    if len(str(p))<2:
        continue
    p_final.append(p)


print(p_final)
print(sum(p_final))