'''


The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2 d3 d4  = 406 is divisible by 2
    d3 d4 d5  = 063 is divisible by 3
    d4 d5 d6  = 635 is divisible by 5
    d5 d6 d7  = 357 is divisible by 7
    d6 d7 d8  = 572 is divisible by 11
    d7 d8 d9  = 728 is divisible by 13
    d8 d9 d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

'''

#generate all pandigitals

pans = []
magicpans =[]
num = ''


range0=[1,2,3,4,5,6,7,8,9]


for i in range0:
    range1=range0.copy()
    range1.append(0)
    range1.remove(i)
    for j in range1:
        range2 = range1.copy()
        range2.remove(j)
        for k in range2:
            range3 = range2.copy()
            range3.remove(k)
            for l in range3:
                range4 = range3.copy()
                range4.remove(l)
                for m in range4:
                    range5 = range4.copy()
                    range5.remove(m)
                    
                    for n in range5:
                        range6 = range5.copy()
                        range6.remove(n)
                        for o in range6:
                            range7 = range6.copy()
                            range7.remove(o)
                            for p in range7:
                                range8 = range7.copy()
                                range8.remove(p)
                                for q in range8:
                                    range9 = range8.copy()
                                    range9.remove(q)
                                    for r in range9:
                                        num = str(i)+str(j)+str(k) \
                                            + str(l)+str(m)+str(n) \
                                            + str(o)+str(p)+str(q) \
                                            + str(r)
                                        pans.append(num)

for pan in pans:
    panstring = str(pan)
    sd2d3d4  = panstring[1:4]
    sd3d4d5  = panstring[2:5]
    sd4d5d6  = panstring[3:6]
    sd5d6d7  = panstring[4:7]
    sd6d7d8  = panstring[5:8]
    sd7d8d9  = panstring[6:9]
    sd8d9d10 = panstring[7:10]
    
    #2,3,5,7,11,13,17

    if int(sd2d3d4)%2 == 0:
        if int(sd3d4d5)%3 == 0:
            if int(sd4d5d6)%5 == 0:
                if int(sd5d6d7)%7 == 0:
                    if int(sd6d7d8)%11 == 0:
                        if int(sd7d8d9)%13 == 0:
                            if int(sd8d9d10)%17 == 0:
                                magicpans.append(int(pan))

print(len(magicpans))
print(sum(magicpans))