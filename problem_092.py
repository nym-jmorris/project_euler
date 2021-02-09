'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

'''
def sqrDigits(number):
    sumnum = 0
    for n in str(number):
        sumnum = sumnum + int(n)**2
    return sumnum

limit = 146

hashtable = {}
final ={}

eighty9s=[]
ones = []

for i in range(1,limit):
    nut = i
    result = 0 
    while result != 1 and result != 89:

        result = sqrDigits(nut)

        if result == 89:
            eighty9s.append(i)
            hashtable.update({i:89})
            for x, y in hashtable.items():
                if y == 0:
                    hashtable.update({x:89})
            
            break
        if result == 1:
            ones.append(i)
            hashtable.update({i:1})
            for x, y in hashtable.items():
                if y == 0:
                    hashtable.update({x:1})
            break

        # if result in hashtable.keys():
        #     result = hashtable[result]
        #     if result == 89:
        #         eighty9s.append(i)
        #     if result == 1:
        #         ones.append(i)
        #     break

        # hashtable.update({result:0})

        nut = result
    final.update({i:result})
    # breakpoint()

print(len(eighty9s))
print(len(ones))

f = open('p092_final.txt','w')
g = open('p092_results.txt','w')
h = open('p092_hash.txt','w')

for key in final.keys():
#    print(str(key)+': '+str(final[key]))
    f.write(str(key)+': '+str(final[key])+'\n')

for key in hashtable.keys():
    h.write(str(key)+': '+str(hashtable[key])+'\n')

g.write('There were {} samples run. {} samples resulted in 89 and {} resulted in 1.'.format(limit-1,len(eighty9s),len(ones)))
g.write('\n{} + {} = {}'.format(len(eighty9s),len(ones),len(eighty9s)+len(ones)))

f.close
g.close
h.close