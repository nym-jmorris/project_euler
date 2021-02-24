'''

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def isPal(number):
    numStr = str(number)
    return numStr==numStr[::-1]

def makeBinary(number):
    i=0
    while True:
        if 2**i < number:
            i+=1
            continue
        break
    
    bina=[]

    for i in range(i,-1,-1):
        q = number // (2**i)
        bina.append(q)
        number = number - q * 2**i
    
    if bina[0]==0:
        bina.pop(0)
    binb = 0

    for i in range(0,len(bina)):
        binb += bina[i]*10**(len(bina)-i-1)

    return binb

dpals = []
uL = 1000000
for i in range(1,uL):
    ibin = makeBinary(i)
    if isPal(i) and isPal(ibin):
#        print('{} is {} in binary. Both are palindromes.'.format(i,ibin))
        dpals.append(i)

print('Sum of palindromes in {}'.format(sum(dpals)))