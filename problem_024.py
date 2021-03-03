'''

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
from itertools import permutations
from time import time

digits = [0,1,2,3,4,5,6,7,8,9]
limit = 1000000

t0 = time()

perms = list(permutations(digits))

strings = []
i = 0
for p in perms:
    string = ''
    for s in p:
        string = string + str(s)
    strings.append(int(string))
    i +=1
    if i>limit:
        break

strings.sort()
t1 = time()
print('The millionth string is {}.\nWe got here in {:.2f} seconds'.format(strings[limit-1],t1-t0))