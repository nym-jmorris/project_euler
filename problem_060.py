'''


The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
# brute force is a bad idea
# Works slowly on three digit primes, as these concatenate to six digit primes...

# what if we start with large primes and split them into 1/2/3/4 digit smaller primes
# then we're searching small primes.  Faster?
# create smaller lists of primes via:
# j2 = [i for i in j if i <= 5]


from math import floor
import time

time0 = time.time()
nmax = 1000000
nmax = 1000

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
    
time2 = time.time()

for p1 in range(0,len(primes)):
    
    for p2 in range(p1+1,len(primes)):
        
        if getSum(int(str(primes[p1])+str(primes[p2]))) % 3 == 0:
            continue
        
        if int(str(primes[p1])+str(primes[p2])) in primes and \
            int(str(primes[p2])+str(primes[p1])) in primes:
            
            print('2 Primes found: {} | {}'.format(primes[p1],primes[p2]))
            print('Time elapsed: {:.2f} seconds\n'.format(time.time()-time2))

            for p3 in range(p2+1,len(primes)):
                if getSum(int(str(primes[p1])+str(primes[p3]))) % 3 == 0:
                    continue
                if getSum(int(str(primes[p2])+str(primes[p3]))) % 3 == 0:
                    continue
                if int(str(primes[p1])+str(primes[p3])) in primes and \
                    int(str(primes[p3])+str(primes[p1])) in primes and \
                        int(str(primes[p2])+str(primes[p3])) in primes and \
                            int(str(primes[p3])+str(primes[p2])) in primes :

                            print('3 Primes found: {} | {} | {}'.format(primes[p1],primes[p2],primes[p3]))
                            print('Time elapsed: {:.2f} seconds\n'.format(time.time()-time2))

                            for p4 in range(p3+1,len(primes)):
                                if getSum(int(str(primes[p1])+str(primes[p4]))) % 3 == 0:
                                    continue
                                if getSum(int(str(primes[p2])+str(primes[p4]))) % 3 == 0:
                                    continue
                                if getSum(int(str(primes[p3])+str(primes[p4]))) % 3 == 0:
                                    continue
                                if int(str(primes[p1])+str(primes[p4])) in primes and \
                                    int(str(primes[p4])+str(primes[p1])) in primes and \
                                        int(str(primes[p2])+str(primes[p4])) in primes and \
                                            int(str(primes[p4])+str(primes[p2])) in primes and \
                                                int(str(primes[p3])+str(primes[p4])) in primes and \
                                                    int(str(primes[p4])+str(primes[p3])) in primes:

                                                    print('4 Primes found: {} | {} | {} | {}'.format(primes[p1],primes[p2],primes[p3],primes[p4]))
                                                    print('Time elapsed: {:.2f} seconds\n'.format(time.time()-time2))

                                                    for p5 in range(p4+1,len(primes)):
                                                        
                                                        if getSum(int(str(primes[p1])+str(primes[p5]))) % 3 == 0:
                                                            continue
                                                        if getSum(int(str(primes[p2])+str(primes[p5]))) % 3 == 0:
                                                            continue
                                                        if getSum(int(str(primes[p3])+str(primes[p5]))) % 3 == 0:
                                                            continue
                                                        if getSum(int(str(primes[p4])+str(primes[p5]))) % 3 == 0:
                                                            continue
                                                        
                                                        if int(str(primes[p1])+str(primes[p5])) in primes and \
                                                            int(str(primes[p5])+str(primes[p1])) in primes and \
                                                                int(str(primes[p2])+str(primes[p5])) in primes and \
                                                                    int(str(primes[p5])+str(primes[p2])) in primes and \
                                                                        int(str(primes[p3])+str(primes[p5])) in primes and \
                                                                            int(str(primes[p5])+str(primes[p3])) in primes and \
                                                                                int(str(primes[p4])+str(primes[p5])) in primes:
                                                                                print('{}, {}, {}, {} and {} meet this condition.'.format(primes[p1],primes[p2],primes[p3],primes[p4],primes[p5]))
                                                                                print('Primes sum to {}'.format(primes[p1]+primes[p2]+primes[p3]+primes[p4]+primes[p5]))
                                                                                print('Computation took {:.2f} seconds'.format(time.time()-time2))
                                                                                break

