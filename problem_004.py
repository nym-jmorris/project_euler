'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''



from math import floor

def isPalindrome(number):
    word = str(number)

    for i in range(0,floor(len(word)/2)+1):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

maxPal = 0 

for i in range(100,1000):
    for j in range (100,1000):
        if isPalindrome(i*j):
            if i*j>maxPal: maxPal = i*j

print(maxPal)