'''

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''
product = 1
for i in range(1,10):
    for j in range(0,10):
        for k in range(1,10):
            for l in range(0,10):
                num = 10*i + j
                denom = 10*k + l

                frac1 = num/denom
                frac2 = 1
                
                if j == k and l!=0 and l!=k:
                    frac2 = i/l
                    if frac1 == frac2:
                        print('{}{}/{}{} == {}/{}'.format(i,j,k,l,i,l))
                        product = product / frac2

# 1/4 * 1/5 * 2/5 * 4/8 = (50*40*80*50)/(200*200*200*200) = 16MM/1.6B = 1/100
# Not sure how I lucked into this being lowest form...
print(product)
