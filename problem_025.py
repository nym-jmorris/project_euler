'''
#problem 25


# The Fibonacci sequence is defined by the recurrence relation:

#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:

#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''

# doing this recursively is too expensive.  It has to call the fib for every number and has no memory.
def fib(n):
    if n ==0:
        return 1
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# computing this directly inside a while loop allows for only one new term to be computed
# during each iteration.

fib0 = 1
fib1 = 1
i = 1

while len(str(fib0))<1000:
    fib2 = fib0+fib1
    fib0 = fib1
    fib1 = fib2
    i += 1

print('{} is the first term with {} digits'.format(i,len(str(fib0))))

