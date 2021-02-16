'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def IsPan(string):
    if len(string)!=9:
        return False
    for i in range(1,10):
        if string.count(str(i))!=1:
            return False
    return True

rng = [1,2,3,4,5,6,7,8,9]

products = []

for i in rng:
    
    rng2 = rng.copy()
    rng2.remove(i)

    for j in rng2:

        rng3 = rng2.copy()
        rng3.remove(j)

        for k in rng3:
            rng4 = rng3.copy()
            rng4.remove(k)

            for l in rng4:
                rng5 = rng4.copy()
                rng5.remove(l)

                for m in rng5:
                    rng6 = rng5.copy()
                    rng6.remove(m)

                    a = i
                    b = 1000*j +100*k + 10*l + m
                    c = a * b

                    if IsPan(str(a)+str(b)+str(c)):
                        products.append(c)
                        print('{} * {} = {}'.format(a,b,c))

                    a = 10*i + j
                    b = 100*k + 10*l + m
                    c = a * b

                    if IsPan(str(a)+str(b)+str(c)):
                        products.append(c)
                        print('{} * {} = {}'.format(a,b,c))

                    
p2=[]

for p in products:
    if p in p2:
        continue
    else: p2.append(p)

print(sum(p2))