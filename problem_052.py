'''

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def isPerm(number1, number2):
    str1 = sorted(str(number1))
    str2 = sorted(str(number2))
    if str1 == str2:
        return True
    else: return False

i = 1
go = True
while go:
    perms = 0
    for m in range(1,7):
        if not isPerm(i,m*i):
            break
        perms += 1
    if perms == 6:
        print('{} is the lowest integer that permutes to x, 2x, 3x, 4x, 5x, 6x'.format(i))
        break
    i += 1
