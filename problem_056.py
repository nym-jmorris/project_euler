'''

A googol (10100) is a massive number: one followed by one-hundred zeros; 
100100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

def digSum(n):
    dsum = 0
    for i in str(n):
        dsum += int(i)
    return dsum

maxdsum = 0
maxa = 0
maxb = 0
top = 100
ith = 0
for a in range(1,top):
    if a%10 == 0: continue
    for b in range(1,top):
        if digSum(a**b)>maxdsum:
            ith += 1
            maxdsum = digSum(a**b)
            maxa = a
            maxb = b
#            print('MaxSum {}:\t{}**{} = {}, with digit sum {}'.format(ith,a,b,a**b,digSum(a**b)))
print('MaxSum Found! {}**{} results in a digit sum of {}'.format(maxa,maxb,digSum(maxa**maxb)))