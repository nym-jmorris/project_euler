'''problem 9


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

triplets = []

def findTriplet():
    for k in range(1,1000):
        for j in range(2,k):
            for i in range(1,j):
                if i+j+k == 1000:

                    if k**2 == i**2 + j**2:
                        
    #                    triplets.append([i,j,k])
                        print('Triplet of {}, sum of {}'.format([i,j,k],i+j+k))
                        print('Magic triplet found!')
                        print('Product is: {}'.format(i*j*k))
                        return([i,j,k])

triplet = findTriplet()