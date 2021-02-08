'''


Bystarting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)

'''

row00=[75]
row01=[95,64]
row02=[17,47,82]
row03=[18,35,87,10]
row04=[20,4,82,47,65]
row05=[19,1,23,75,3,34]
row06=[88,2,77,73,7,63,67]
row07=[99,65,4,28,6,16,70,92]
row08=[41,41,26,56,83,40,80,70,33]
row09=[41,48,72,33,47,32,37,16,94,29]
row10=[53,71,44,65,25,43,91,52,97,51,14]
row11=[70,11,33,28,77,73,17,78,39,68,17,57]
row12=[91,71,52,38,17,14,91,43,58,50,27,29,48]
row13=[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
row14=[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

sum = 0

f = open('p18_output.txt','w')

maxsumpath =0

for i in range(0,len(row00)):
    for j in range(i,i+2):
        for k in range(j,j+2):
            for l in range(k,k+2):
                for m in range(l,l+2):
                    for n in range(m,m+2):
                        for o in range(n,n+2):
                            for p in range(o,o+2):
                                for q in range(p,p+2):
                                    for r in range(q,q+2):
                                        for s in range(r,r+2):
                                            for t in range(s,s+2):
                                                for u in range(t,t+2):
                                                    for v in range(u,u+2):
                                                        for w in range(v,v+2):

                                                            # print('Row00: '+ str(row00[i]) +
                                                            # '\nRow01: '+str(row01[j])+
                                                            # '\nRow02: '+str(row02[k])+
                                                            # '\nRow03: '+str(row03[l])+
                                                            # '\n')
                                                            f.write('Row00: '+ str(row00[i]) +
                                                            '\nRow01: '+str(row01[j])+
                                                            '\nRow02: '+str(row02[k])+
                                                            '\nRow03: '+str(row03[l])+
                                                            
                                                            '\nRow04: '+str(row04[l])+
                                                            '\nRow05: '+str(row05[l])+
                                                            '\nRow06: '+str(row06[l])+
                                                            '\nRow07: '+str(row07[l])+
                                                            '\nRow08: '+str(row08[l])+
                                                            '\nRow09: '+str(row09[l])+
                                                            '\nRow10: '+str(row10[l])+
                                                            '\nRow11: '+str(row11[l])+
                                                            '\nRow12: '+str(row12[l])+
                                                            '\nRow13: '+str(row13[l])+
                                                            '\nRow14: '+str(row14[l])+

                                                            '\n\n')

                                                            sumpath = row00[i]+row01[j]+row02[k]+row03[l]\
                                                                + row04[m] + row05[n] + row06[o] + row07[p] \
                                                                    + row08[q] + row09[r] + row10[s] + row11[t]\
                                                                         + row12[u] + row13[v] + row14[w] 
                                                            if sumpath > maxsumpath:
                                                                maxsumpath = sumpath
                                                                # maxpath = 'Row00: '+ str(row00[i]) +\
                                                                # '\nRow01: '+str(row01[j])+\
                                                                # '\nRow02: '+str(row02[k])+\
                                                                # '\nRow03: '+str(row03[l])+\
                                                                # '\nRow04: '+str(row04[l])+\
                                                                # '\nRow05: '+str(row05[l])+\
                                                                # '\nRow06: '+str(row06[l])+\
                                                                # '\nRow07: '+str(row07[l])+\
                                                                # '\nRow08: '+str(row08[l])+\
                                                                # '\nRow09: '+str(row09[l])+\
                                                                # '\nRow10: '+str(row10[l])+\
                                                                # '\nRow11: '+str(row11[l])+\
                                                                # '\nRow12: '+str(row12[l])+\
                                                                # '\nRow13: '+str(row13[l])+\
                                                                # '\nRow14: '+str(row14[l])

f.close()
print(maxsumpath)
#print(maxpath)