
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding 
these values we form a word value. 

For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 

If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?


'''



import csv

with open('p042_words.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


words = data[0].copy()

# for word in words:
#     print(word)


triangles = []
mwords = []

for i in range(1,100):
    triangles.append(int(0.5*i*(i+1)))

for word in words:
    wordval = 0
    for letter in word:
        wordval = wordval+ord(letter)-64
    if wordval in triangles:
#        print(word + ' is a triangle word')
        mwords.append(word)
print('There are '+ str(len(mwords))+ ' triangle words')
