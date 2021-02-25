'''

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

megasum = 0

for i in range(1,1000):
    megasum = (megasum + i**i%10**10)%10**10

print('{:,d}'.format(megasum))