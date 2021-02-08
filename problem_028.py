'''

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

from math import floor

size = 1001
size = 5
spiral = [[0 for i in range(size)] for j in range(size)]


for i in range(0,size):
    print(spiral[i][:])

print('\n')


pos_x = int(floor(size/2))
pos_y = int(floor(size/2))

spiral[pos_x][pos_y]=1

move_last = 'left'
#move_next = 'right'

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
    if move_last == 'left' and spiral[pos_x-1][pos_y]!=0:
        spiral[pos_x-1][pos_y]=i
        pos_x = pos_x-1
        move_last = 'left'
        

for i in range(0,size):
    print(spiral[i][:])