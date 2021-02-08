'''#problem 22


# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

'''
import csv

import string


with open('p022_names.txt', newline='') as f:
    reader = csv.reader(f)
    
    data = list(reader)

nameList = data[0]

nameList.sort()


namesum = 0
position = 0
namescore = 0

for i in range (0,len(nameList)):
    namesum = 0
    position += 1
    for j in range(0,len(nameList[i])):
        namesum += (string.ascii_uppercase.index(nameList[i][j]))+1
    #print('Name = {:>10}, position = {}, nameScore = {}, combinedScore = {}, running score = {}.'.format(nameList[i],position,namesum,position*namesum,namescore + namesum*position))
    namescore += namesum * position
    
print(namescore)
