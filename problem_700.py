'''


Leonhard Euler was born on 15 April 1707.

Consider the sequence 1504170715041707n mod 4503599627370517.

An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first Eulercoin. 
The second term is 3008341430083414 which is greater than 1504170715041707 so is not an Eulercoin. 
However, the third term is 8912517754604 which is small enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins.
'''

# brute force will take too long
# what else can be done re: modulo math?

coins = [1504170715041707]
i = 0

upper = 750000000

for i in range (1,upper):
    x= ((1504170715041707 * i) % 4503599627370517 )
    if x < coins[len(coins)-1]:
        coins.append(x)
    if i%100000000==0:
        print('Passing '+str(i) + ' evaluations.')


print(coins)
print('Sum of coins is '+str(sum(coins)))