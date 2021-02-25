'''

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

# don't need to build a new spiral every time, just layer in the new numbers
# don't even need that; just layer in the new corners.


def isPrime(n):
    p = 2
    if n<2:
        return False
    while p * p <= n:
        if n%p==0:
            return False
        p+=1
    return True

go = True
size = 7



while go:
    spiral = [[0 for i in range(size)] for j in range(size)]

    pos_x = size//2
    pos_y = size//2

    spiral[pos_x][pos_y]=1
    move_last = 'left'

    for i in range(2,size*size+1):

        if move_last == 'up' and spiral[pos_x+1][pos_y]==0:
            spiral[pos_x+1][pos_y]=i
            pos_x = pos_x + 1
            move_last = 'right'
            
            continue
        if move_last == 'up' and spiral[pos_x+1][pos_y]!=0:
            spiral[pos_x][pos_y+1]=i
            pos_y = pos_y+1
            move_last = 'up'
            
            continue

        if move_last == 'right' and spiral[pos_x][pos_y-1]==0:
            spiral[pos_x][pos_y-1]=i
            pos_y = pos_y-1
            move_last = 'down'
            
            continue
        if move_last == 'right' and spiral[pos_x][pos_y-1]!=0:
            spiral[pos_x+1][pos_y]=i
            pos_x = pos_x+1
            move_last = 'right'
            
            continue

        if move_last == 'down' and spiral[pos_x-1][pos_y]==0:
            spiral[pos_x-1][pos_y]=i
            pos_x = pos_x-1
            move_last = 'left'
            
            continue
        if move_last == 'down' and spiral[pos_x-1][pos_y]!=0:
            spiral[pos_x][pos_y-1]=i
            pos_y = pos_y-1
            move_last = 'down'
            
            continue

        if move_last == 'left' and spiral[pos_x][pos_y+1]==0:
            spiral[pos_x][pos_y+1]=i
            pos_y = pos_y+1
            move_last = 'up'
            
            continue
        if move_last == 'left' and spiral[pos_x][pos_y+1]!=0:
            spiral[pos_x-1][pos_y]=i
            pos_x = pos_x-1
            move_last = 'left'
            
            continue

    primes = 0
    for i in range(0,size):
        if isPrime(spiral[i][i]):
            primes += 1
        if isPrime(spiral[i][size-i-1]):
            primes += 1
        if isPrime(spiral[size//2][size//2]):
            primes -= 1

    ratio = primes / (2 * size - 1)
    #print('Side size of {} yields ratio of {}'.format(size,ratio))
    if ratio < 0.10:
        break
    size += 2

print('The prime diagonal ratio drops below 10% when the spiral has a side of length {}'.format(size))