'''

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

digits = [0,1,2,3,4,5,6,7,8,9]
d1 = digits.copy()

perms =[]

for i in d1:
    d2 = d1.copy()
    d2.remove(i)
    
    for j in d2:
        d3 = d2.copy()
        d3.remove(j)

        for k in d3:
            d4 = d3.copy()
            d4.remove(k)

            for l in d4:
                d5 = d4.copy()
                d5.remove(l)

                for m in d5:
                    d6 = d5.copy()
                    d6.remove(m)

                    for n in d6:
                        d7 = d6.copy()
                        d7.remove(n)

                        for o in d7:
                            d8 = d7.copy()
                            d8.remove(o)

                            for p in d8:
                                d9 = d8.copy()
                                d9.remove(p)
                                
                                for q in d9:
                                    d10 = d9.copy()
                                    d10.remove(q)

                                    for r in d10:
                                        perm = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)
                                        perms.append(perm)

perms.sort()
print(perms[999999])

