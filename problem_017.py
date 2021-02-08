'''
# problem 17


# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.
'''
from math import floor

def numParse(number):
    part2 = ''
    part2 = ''
    part1 = ''
    
    ones = 0
    teens = 0
    tens = 0
    hundreds = 0

    if number >= 100:
        hundreds = int(floor(number/100))
    if number - 100 * hundreds >= 20:
        tens = int(floor((number - hundreds * 100)/10))
    if number - 100 * hundreds >= 10 and number - 100 * hundreds < 20:
        teens = number - 100 * hundreds
    if number - 100 * hundreds - 10 * tens > 0 and teens ==0:
        ones = number - 100 * hundreds - 10 * tens 
    


    if hundreds == 0:
        part1 = ''
    elif hundreds == 1:
        part1 = 'one'
    elif hundreds == 2:
        part1 = 'two'
    elif hundreds == 3:
        part1 = 'three'
    elif hundreds == 4:
        part1 = 'four'
    elif hundreds == 5:
        part1 = 'five'
    elif hundreds == 6:
        part1 = 'six'
    elif hundreds == 7:
        part1 = 'seven'
    elif hundreds == 8:
        part1 = 'eight'
    else: part1 = 'nine'

    if part1 == '':
        part1 = ''
    else: part1 = part1 + 'hundred'

    if tens == 0 and teens == 0 and ones == 0:
        part2 = ''
        part2 = ''
    elif teens != 0:
        if teens == 10:
            part2 = 'ten'
        elif teens == 11:
            part2 = 'eleven'
        elif teens == 12:
            part2 = 'twelve'
        elif teens == 13:
            part2 = 'thirteen'
        elif teens == 14:
            part2 = 'fourteen'
        elif teens == 15:
            part2 = 'fifteen'            
        elif teens == 16:
            part2 = 'sixteen'
        elif teens == 17:
            part2 = 'seventeen'
        elif teens == 18:
            part2 = 'eighteen'            
        else:part2 = 'nineteen'
    else:
        if tens ==2:
            part2 = 'twenty'
        elif tens ==3:
            part2 = 'thirty'
        elif tens ==4:
            part2 = 'forty'
        elif tens ==5:
            part2 = 'fifty'
        elif tens ==6:
            part2 = 'sixty'
        elif tens ==7:
            part2 = 'seventy'
        elif tens ==8:
            part2 = 'eighty'
        elif tens ==9:
            part2 = 'ninety'
        else: part2 =''

    if ones ==0:
        part3 = ''
    else:
        if ones ==1:
            part3 = 'one'
        elif ones ==2:
            part3 = 'two'
        elif ones ==3:
            part3 = 'three'
        elif ones ==4:
            part3 = 'four'
        elif ones ==5:
            part3 = 'five'
        elif ones ==6:
            part3 = 'six'
        elif ones ==7:
            part3 = 'seven'                                                
        elif ones ==8:
            part3 = 'eight'
        else:
            part3 = 'nine'
    
    output = ''

    if part1 != '' and (part2 != '' or part3 !=''):
        output = part1+'and'+part2+part3
    else: output = part1+part2+part3

    #print(output)

    #print(len(part1)+len(part2)+len(part3))

    #print(len(output))
    #longword += len(output)
    return output, len(output)

    #print('{} breaks down into {} hundreds, {} tens, {} teens and {} ones.'.format(number,hundreds,tens,teens,ones))

longword = 0



for i in range(1,1000):
    word = numParse(i)
#    print('{:>3}: {:>20}'.format(str(i),word[0]))
    longword += word[1]

# one thousand == 11 characters...
print(longword+11)
