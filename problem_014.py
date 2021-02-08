'''
#problem 14


# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

'''

import time
time_start = time.time()

def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1

point = 1000

maxlen = 0
maxnum = 0

for j in range(2,1000000):
#n = 13
    n = j
    point = n
    chain = []

    while point != 1:
        point = collatz(point)
        chain.append(point)
    #print('\n {:>6} complete. Chainlength of {:>3}.'.format(j,len(chain)))
    if len(chain)>maxlen:
        maxlen = len(chain)
        maxnum = j


print('The starting number with the longest chain is {}, with a chainlength of {}'.format(maxnum,maxlen))
print('Time elapsed: {:06.2f} seconds'.format(time.time()-time_start))