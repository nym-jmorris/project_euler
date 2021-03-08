'''


The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
# brute force works, but can definitely be made better.

# what if we start with large primes and split them into 1/2/3/4 digit smaller primes
# then we're searching small primes.  Faster?
# create smaller lists of primes via:
# j2 = [i for i in j if i <= 5]


# 
# 13, 5197, 5701, 6733 and 8389 meet this condition.
# Primes sum to 26033
# Computation took 66.06 seconds

from math import floor
import time

time0 = time.time()
nmax = 1000000
nmax = 10000

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
print('{} primes generated in {:.2f} seconds\n'.format(len(primes),time.time()-time1))

def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum

def isPrime(n):
    p = 2
    if n<2:
        return False
    while p * p <= n:
        if n%p==0:
            return False
        p+=1
    return True

def concat(n,m):
    return int(str(n)+str(m))

time2 = time.time()

p1 = 0


while p1 < len(primes):
    p2 = p1+1
    while p2 < len(primes):
        if getSum(concat(primes[p1],primes[p2])) % 3 == 0:
            p2 += 1
            continue
        
        if isPrime(concat(primes[p1],primes[p2])) and \
            isPrime(concat(primes[p2],primes[p1])):
            
            # print('2 Primes found: {} | {}'.format(primes[p1],primes[p2]))
            # print('Time elapsed: {:.2f} seconds\n'.format(time.time()-time2))

            p3 = p2+1

            while p3 < len(primes):
                

                if getSum(concat(primes[p1],primes[p3])) % 3 == 0:
                    p3 += 1
                    continue
                if getSum(concat(primes[p2],primes[p3])) % 3 == 0:
                    p3 += 1
                    continue
                if isPrime(concat(primes[p1],primes[p3])) and \
                    isPrime(concat(primes[p3],primes[p1])) and \
                        isPrime(concat(primes[p2],primes[p3])) and \
                            isPrime(concat(primes[p3],primes[p2])):

                            # print('3 Primes found: {} | {} | {}'.format(primes[p1],primes[p2],primes[p3]))
                            # print('Time elapsed: {:.2f} seconds\n'.format(time.time()-time2))

                            p4 = p3+1

                            while p4 < len(primes):

                                if getSum(concat(primes[p1],primes[p4])) % 3 == 0:
                                    p4 += 1
                                    continue
                                if getSum(concat(primes[p2],primes[p4])) % 3 == 0:
                                    p4 += 1
                                    continue
                                if getSum(concat(primes[p3],primes[p4])) % 3 == 0:
                                    p4 += 1
                                    continue
                                if isPrime(concat(primes[p1],primes[p4])) and \
                                    isPrime(concat(primes[p4],primes[p1])) and \
                                        isPrime(concat(primes[p2],primes[p4])) and \
                                            isPrime(concat(primes[p4],primes[p2])) and \
                                                isPrime(concat(primes[p3],primes[p4])) and \
                                                    isPrime(concat(primes[p4],primes[p3])):
                                                    
                                                    # print('4 Primes found: {} | {} | {} | {}'.format(primes[p1],primes[p2],primes[p3],primes[p4]))
                                                    # print('Time elapsed: {:.2f} seconds\n'.format(time.time()-time2))

                                                    p5 = p4 + 1

                                                    while p5 < len(primes):
                                                        
                                                        if getSum(concat(primes[p1],primes[p5])) % 3 == 0:
                                                            p5 += 1
                                                            continue
                                                        if getSum(concat(primes[p2],primes[p5])) % 3 == 0:
                                                            p5 += 1
                                                            continue
                                                        if getSum(concat(primes[p3],primes[p5])) % 3 == 0:
                                                            p5 += 1
                                                            continue
                                                        if getSum(concat(primes[p4],primes[p5])) % 3 == 0:
                                                            p5 += 1
                                                            continue
                                                        
                                                        if isPrime(concat(primes[p1],primes[p5])) and \
                                                            isPrime(concat(primes[p5],primes[p1])) and \
                                                                isPrime(concat(primes[p2],primes[p5])) and \
                                                                    isPrime(concat(primes[p5],primes[p2])) and \
                                                                        isPrime(concat(primes[p3],primes[p5])) and \
                                                                            isPrime(concat(primes[p5],primes[p3])) and \
                                                                                isPrime(concat(primes[p4],primes[p5])) and \
                                                                                    isPrime(concat(primes[p5],primes[p4])):
                                                                                    print('{}, {}, {}, {} and {} meet this condition.'.format(primes[p1],primes[p2],primes[p3],primes[p4],primes[p5]))
                                                                                    print('Primes sum to {}'.format(primes[p1]+primes[p2]+primes[p3]+primes[p4]+primes[p5]))
                                                                                    print('Computation took {:.2f} seconds'.format(time.time()-time2))
                                                                                    p5 = len(primes)
                                                                                    p4 = len(primes)
                                                                                    p3 = len(primes)
                                                                                    p2 = len(primes)
                                                                                    p1 = len(primes)
                                                                                    break
                                                        p5 +=1
                                p4 += 1
                p3 += 1
        p2 += 1
    p1 += 1