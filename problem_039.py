'''

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from math import floor

triangles =[]

limit = 1001

amax = int(floor(limit/2))+1

for a in range(1,amax+1):
    for b in range(a,amax+1):
        for c in range(b,amax+1):
            #breakpoint()
            if a**2+b**2 == c**2 and a+b+c <= limit:
                triangles.append([a,b,c])


#print(triangles)

dict_results = {}

for t in triangles:
    sumt = sum(t)
#    print(str(sumt)+': '+str(t))
    if sumt in dict_results.keys():
        dict_results.update({sumt:dict_results[sumt]+1})
    else:  dict_results.update({sumt:1})

maxval = 0
maxkey = 0 

for key in dict_results.keys():
    #print(str(key)+': '+ str(dict_results[key]))
    if dict_results[key]> maxval:
        maxval = dict_results[key]
        maxkey = key
        

print('\nThere are ' +str(maxval) +' triangles when the path has perimeter of '+str(maxkey))


