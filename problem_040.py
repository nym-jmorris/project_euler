'''

An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910 1 112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

string = '.'

for i in range(1,500000):
    string = string + str(i)

product = 1

for i in range (0,7):
    try:
        dstr = 'd'+str(10**i)
        print('{:>8}:\t{}'.format(dstr,string[10**i]))
        product = product * int(string[10**i])
    except IndexError:
        print('Busted')

print('Product of terms is: {}'.format(product))

