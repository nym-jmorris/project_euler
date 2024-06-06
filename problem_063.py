'''

Problem 63

The
-digit number, , is also a fifth power. Similarly, the -digit number,

, is a ninth power.

How many
-digit positive integers exist which are also an th power?
'''

matches = []

for i in range(1,10):
    for p in range(1,22):
        # print(i**p)
        if len(str(i**p)) == p:
            matches.append(i**p)


print(matches)
print(len(matches))