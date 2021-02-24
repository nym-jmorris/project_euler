'''

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def IsPan(string):
    if len(string)!=9:
        return False
    for i in range(1,10):
        if string.count(str(i))!=1:
            return False
    return True

# must start with 9..
# must be at least 1,2

candidates = []
lefts = []

for i in range(9,10):
    left = i
    lefts.append(left)

for i in range(0,10):
    left = 90 + i
    lefts.append(left)
    

for i in range(0,10):
    for j in range(0,10):
        left = 900 + 10*i + j
        lefts.append(left)

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            left = 9000 + 100*i + 10*j + k
            lefts.append(left)

# for left in lefts:
#     print(left)

maxpan = 0
maxleft = 0
maxgroup = 0 

for left in lefts:
    for groupsize in range(1,7):
        candidate = ''
        for i in range(1,groupsize):
            candidate = candidate + str(left * i)
        if len(candidate)==9 and IsPan(candidate):
            print('Candidate found: {} with group size {} yields: {}'.format(left,groupsize-1,candidate))
            candidates.append(candidate)
            if int(candidate)>maxpan:
                maxpan = int(candidate)
                maxleft = left
                maxgroup = groupsize-1

print('The largest pandigital is {}, which is the result of {} with a group size of {}'.format(maxpan,maxleft,maxgroup))
        
