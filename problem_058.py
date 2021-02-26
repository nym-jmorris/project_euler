'''

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

# don't need to build a new spiral every time, just layer in the new numbers
# don't even need that; just layer in the new corners.

# don't even need a spiral!

def isPrime(n):
    p = 2
    if n<2:
        return False
    while p * p <= n:
        if n%p==0:
            return False
        p+=1
    return True

limit = 0.10
go = True
lastd = 1

diags = [1]
pdiags = []

size = 3
while go:

    d1 = lastd + (size-1)
    d2 = lastd + 2*(size-1)
    d3 = lastd + 3*(size-1)
    d4 = lastd + 4*(size-1)

    if isPrime(d1):
        pdiags.append(d1)
    if isPrime(d2):
        pdiags.append(d2)
    if isPrime(d3):
        pdiags.append(d3)
    if isPrime(d4):
        pdiags.append(d4)
    
    diags.append(d1)
    diags.append(d2)
    diags.append(d3)
    diags.append(d4)

    lastd = d4
    ratio = len(pdiags)/len(diags)

    if ratio > limit:
        size += 2
    else: break

print('A spiral of size {} has a ratio of {:.2f}, which is lower than our limit of {:.2f}'.format(size,ratio,limit))