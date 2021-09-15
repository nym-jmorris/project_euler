

# Problem 66

# Consider quadratic Diophantine equations of the form:

# x**2 – Dy**2 = 1

# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 3**2 – 2 × 2**2 = 1
# 2**2 – 3 × 1**2 = 1
# 9**2 – 5 × 4**2 = 1
# 5**2 – 6 × 2**2 = 1
# 8**2 – 7 × 3**2 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


# checks for perfect square
# babylonian algorithm

def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return [False, None]
        seen.add(x)
    return [True, x]

n = 9
d_list = [iter for iter in range(2,n)]

for d in d_list:
    if is_square(d)[0]:
        d_list.remove(d)

#d_list now has no squares
print(d_list)

