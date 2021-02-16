'''

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

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

# Find the prime factors of an integer:
def factorize(n):
    factors = []
    i = 0
    p = primes[i]

    while p <= n:
        while n % p == 0:
            factors.append(p)
            n = n // p
        if n == 1:
            break
        i += 1
        p = primes[i]
    return factors

def uniquify(array):
    ua = []
    for a in array:
        if a in ua:
            continue
        ua.append(a)
    return len(ua)

dict_dist_primes={}

lower = 10
upper = ceiling

print('Factorization begining')

for i in range(lower, upper):
    factors = factorize(i)
    dict_dist_primes.update({i:uniquify(factors)})

    if i>=lower+3:
        if dict_dist_primes[i]==4 and dict_dist_primes[i-1]==4 and dict_dist_primes[i-2]==4 and dict_dist_primes[i-3]==4:
            print('{}, {}, {}, {} meet this sequence'.format(i-3,i-2,i-1,i))
            break

    if i%(ceiling//10)==0:
        print('Passing {} numbers factored'.format(i))
