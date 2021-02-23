'''
#problem 30


# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#     1634 = 1**4 + 6**4 + 3**4 + 4**4
#     8208 = 8**4 + 2**4 + 0**4 + 8**4
#     9474 = 9**4 + 4**4 + 7**4 + 4**4

# As 1 = 1**4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
# how to set an upper limit for this?
# looking to p34...


# From the forums once I brute forced it...
# The maximum value for one digit is 9^5 = 59,049. 
# We can find out the maximum possible sum for a given number of digits by multiplying 59,049 with the number of digits.
# Let's say we're gonna check the number 123,456,789. 
# That's 9 digits, so the maximum sum would be 9*59,049 = 531,441, which doesn't even come close to 123,456,789. 
# So we know we can forget about any number 9-digit number because we'll never be able to reach a big enough sum. 
# And it'll only get worse with larger numbers...

# 999 => 9**3 = 729
# 729 x 3 = 2,187
# 
# # 9,999 => 9**4 = 6,561
# 4 x 9**4 = 26,244
#
# # 99,999 => 9**5 = 54,049
# 5 x 9**5 = 295,245
# 
# # 999,999 => 9**6 = 531,441
# 6 x 9**6 = 3,188,646




def fifthify(number):
    sums = 0
    num_str = str(number)
    for a in num_str:
        sums = sums + int(a)**5
    return sums


fifths = []

for i in range(2,9**6+1):
    if fifthify(i)==i:
        print('{} meets the condition'.format(i))
        fifths.append(i)

print('sum of fifths = {}'.format(sum(fifths)))