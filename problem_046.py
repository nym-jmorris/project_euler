'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

# checks for perfect square
# babylonian algorithm
def is_square(apositiveint):
    if apositiveint == 1: return [True,1]
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return [False, None]
        seen.add(x)
    return [True, x]

ceiling = 200000

#  Find all primes below the ceiling via Sieve of Eratosthenes:
nmax = ceiling

primes = []

candidates = [True for iter in range(nmax)]

def updateSieve(prime):
    for i in range(0,nmax // prime):
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

# for n, 
# for primes less than not
# can we find m such that m**2 == (n-p)/2
primes.pop(0)
i = 9
go = True
while go:
#while i<10:
    if i%10001==0: print('Testing {:,d}'.format(i))
    for p in primes:
        if p>i: 
            print('Primes exhausted. {} is the boogieman.'.format(i))
            go = False
            break
        isq = is_square(int((i-p)/2))
        if isq[0]:
            i += 2
            break
        # print('Testing {}.  Currently testing prime: {}. Is ({}-{})/2 = {} a perfect square?'.format(i,p,i,p,int((i-p)/2)))
        # print('{} is square: {}'.format(int((i-p)/2),is_square(int((i-p)/2))[0]))

print('First number to fail is {}.'.format(i))