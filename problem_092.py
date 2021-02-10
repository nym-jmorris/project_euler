'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

'''

from time import time

ts = time()

def sqrDigits(number):
    sumnum = 0
    for n in str(number):
        sumnum = sumnum + int(n)**2
    return sumnum

limit = 10000001

hashtable = {}
final ={}

for i in range(1,limit):
    zeros =[]
    nut = i
    try:
        result = hashtable[i]
    except KeyError:
        result = 0
    
    while result != 1 and result != 89:

        zeros = list(dict.fromkeys(zeros))

        result = sqrDigits(nut)
        nut = result

        if result == 89:
            hashtable.update({i:89})
            # This method is very slow.  
            # Replaced with the list of zeros below.
            # for x, y in hashtable.items():
            #     if y == 0:
            #         hashtable.update({x:89})
            for z in zeros:
                hashtable.update({z:89})
            break

        if result == 1:
            hashtable.update({i:1})
            for z in zeros:
                hashtable.update({z:1})
            break

        try:
            if hashtable[result] !=0:
                result = hashtable[result]
                break
        except KeyError:
            hashtable.update({i:0})
            zeros.append(i)

        hashtable.update({result:0})
        zeros.append(result)
 
    final.update({i:result})
 
    for z in zeros:
        hashtable.update({z:result})

tf = time()

print('Program execution took {:.3f} seconds start to finish.'.format(tf-ts))

ones = 0 
eighty9s =0

for x, y in final.items():
    if y == 1:
        ones+=1
    if y == 89:
        eighty9s+=1

print(eighty9s)
print(ones)

g = open('p092_results.txt','w')
h = open('p092_hash.txt','w')

for key in hashtable.keys():
    h.write(str(key)+': '+str(hashtable[key])+'\n')

g.write('There were {} samples run. {} samples resulted in 89 and {} resulted in 1.'.format(limit-1,eighty9s,ones))
g.write('\n{} + {} = {}'.format(eighty9s,ones,eighty9s+ones))

g.close
h.close