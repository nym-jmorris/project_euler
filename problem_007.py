'''problem 7


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time
start_time = time.time()


primes = [2]
checked = [2]
composites = []

#print(len(primes))

pin = 3

while len(primes)<10001:
    for p in range(0,len(primes)-1):
        if pin%primes[p] == 0:
            composites.append(pin)
    # if pin in composites:
    #     continue
    if pin not in composites:
        primes.append(pin)
        if len(primes)%1000==0:
            print('Passing prime # {}'.format(len(primes)))
            print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
            print('Prime density: {}'.format(len(primes)/pin))
    pin+=2
    composites = []

print('The {}th prime is {}.'.format(len(primes),primes[len(primes)-1]))
print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
print('Prime density: {}'.format(len(primes)/primes[len(primes)-1]))