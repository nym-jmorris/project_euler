'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

1 + 1/(2+1/(2+1/(2+...)))

By expanding this for the first four iterations, we get:
1.5
1.4
1.4166...
1.41379...

The next three expansions are 99/70, 239/169, 577/408, but the eighth expansion, 1393/985, 
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
'''

#numerators:
#3,7,17,41, pattern = 2(n-1) + (n-2)

# #denominators:
#2,5,12,29, pattern == 2(n-1) + (n-2)


numes = [3,7]
denoms = [2,5]

longnums = 0

for i in range(2,1000):
    numes.append(2 * numes[i-1] + numes[i-2])
    denoms.append(2 * denoms[i-1] + denoms[i-2])

    numerator = numes[i]
    denominator = denoms[i]
    if len(str(numerator))>len(str(denominator)):
        longnums += 1

print('Long Nums = {}'.format(longnums))
