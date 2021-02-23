'''


Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''
# This would work, but would take forever.
# define HCF
# build dictionary of {n/d:[n,d]}
# list = list(dict.keys())
# i = list.index(3/7)
# return list[i-1]


# instead of building out all the numbers, just focus on whatever comes between 3/7 and it's current neighbor...

def hcf(n,d):
    
    while True:
        q = d//n
        r = d-q*n
        if r==0:
            return n
        d = n
        n = r


pin = 3/7
best = 2/5
upper = 1000000
bdict = {best:[2,5]}

for n in range(8,upper+1):
    inc = 1/n
    q = int(pin // inc)
    if hcf(q,n)==1:
        if pin - q/n < pin - best:
            best = q/n
            bdict.update({best:[q,n]})
print('For n = {:7,d} the leftmost neighbor is {}/{}'.format(n,bdict[best][0],bdict[best][1]))