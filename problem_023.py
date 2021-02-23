'''

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. 

For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. 

However, this upper limit cannot be reduced any further by analysis even though 
it is known that the greatest number that cannot be expressed as the sum of two 
abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
'''

from time import time

def getfactors(n):
    factors = [1]
    for i in range(2,n//2+1):
        if n%i==0:
            factors.append(i)
    return factors

def isAbundant(n,factors):
    if sum(factors)>n:
        return True
    else: return False

limit = 28123
#limit = 5000
abundants = []
nopes = []

print('Starting search for abundant numbers...')
time0 = time()
for i in range(1,limit+1):
    if isAbundant(i,getfactors(i)):
        abundants.append(i)
time1 = time()


print('\nThere are {} abundant numbers under {}.'.format(len(abundants),limit+1))
print('Abundant numbers were generated in {:.2f} seconds'.format(time1-time0))

def makeNum(n):
    uL = 0

    # find the upper bound for a. a can't be greater than n.
    for i in range(0, len(abundants)):
        if abundants[i] < n:
            uL = i
        else:
            break

    for i in range(0,uL):
        for j in range(0,uL):
            if n == abundants[i] + abundants[j]:
#                print('{} = {} + {}'.format(n,abundants[i],abundants[j]))
                return True
    return False


# for i in range(1,limit+1):
#     if makeNum(i) != True:
#         nopes.append(i)
time2 = time()

# print('The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {}'.format(sum(nopes)))
# print('All nopes found in {:.2f} seconds'.format(time2-time1))

print('\nBuilding all combinations of abundant numbers under the limit...')
ytemp = []
for i in range(0,len(abundants)):
    for j in range(0,len(abundants)):
        if abundants[i]+abundants[j] < limit+1:
            ytemp.append(abundants[i]+abundants[j])

time3 = time()

ytemp.sort()

yups=[24]

i=0
for y in ytemp:
    if yups[i] < y:
        yups.append(y)
        i+=1
        
time4= time()

print('\nThere are {} sums to be generated from adding among the {} abundants'.format(len(ytemp),len(abundants)))
print('This took {:.2f} seconds\n'.format(time3-time2))

print('There are {} unique sums to be generated from adding amoung the {} abundants'.format(len(yups),len(abundants)))
print('This took {:.2f} seconds'.format(time4-time3))

time5=time()
num = 1

def popGap(yup1,yup2):
    for i in range(1,yup2-yup1):
        nopes.append(yup1+i)

for i in range(1,yups[0]):
    nopes.append(i)

for i in range(0,len(yups)-1):
    if yups[i+1]-yups[i]>1:
#        print('There is a gap between {} and {}'.format(yups[i],yups[i+1]))
        popGap(yups[i],yups[i+1])

time6=time()
print('\nThere are {} numbers below {} that cannot be expressed as the sum of two abundant numbers'.format(len(nopes),sum(nopes)))
print('This took {:.2f} seconds'.format(time6-time5))
#print(nopes[0:25])
print('Full process took {:.2f} seconds'.format(time6-time0))
print('Sum of non-expressable integers is {}'.format(sum(nopes)))