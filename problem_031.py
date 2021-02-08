'''# problem 31

# In the United Kingdom the currency is made up of pound (£) and pence (p). 
# There are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

'''
ways = 0

needed = 200

for a in range(0,int(needed/100) + 1):
    for b in range(0,int((needed-a*100)/50)+1):
        for c in range(0,int((needed-a*100-b*50)/20)+1):
            for d in range(0,int((needed-a*100-b*50-c*20)/10)+1):
                for e in range(0,int((needed-a*100-b*50-c*20-d*10)/5)+1):
                    for f in range(0,int((needed-a*100-b*50-c*20-d*10-e*5)/2)+1):
                        for g in range(0,int((needed-a*100-b*50-c*20-d*10-e*5-f*2)/1)+1):
                            if 100*a + 50*b + 20*c + 10*d + 5*e + 2*f + 1*g == 200:
                                print('1£: {}, 50p: {} 20p: {} 10p: {} 5p:{} 2p: {} 1p: {}'.format(a,b,c,d,e,f,g))
                                ways+=1
print(ways+1) # +1 for the 2£ coin.