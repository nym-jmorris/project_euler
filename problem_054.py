#Problem 54
# In the card game poker, a hand consists of five cards and are ranked, 
# from lowest to highest, in the following way:

#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; 
# for example, a pair of eights beats a pair of fives (see example 1 below). 
# But if two ranks tie, for example, both players have a pair of queens, 
# then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
# 	 	2C 3S 8S 8D TD
# Pair of Eights
# 	 	Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
# 	 	2C 5C 7D 8S QH
# Highest card Queen
# 	 	Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
# 	 	3D 6D 7D TD QD
# Flush with Diamonds
# 	 	Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
# 	 	3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
# 	 	Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
# 	 	3C 3D 3S 9S 9D
# Full House
# with Three Threes
# 	 	Player 1

# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): the first five 
# are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or repeated cards), 
# each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

#what we need:
    # Split hands
    # Evaluate hands
    # flushStraight
    # 4/3/2pair/1pair
    # FullHouse
    # Nothing
    # Three high cards
        # Full House: Dominant 3, Pair, Zero
        # Straight: High Card, Zero, Zero
        # Flush: High, 2 High, 3 High
        # FourKind: Four Card, One Card, Zero
        # ThreeKind: Three Card, High Card, 2 High
        # Two Pair: High Pair, Low Pair, One Card
        # One Pair: Pair, High Card, 2 High
        # Nothing: High, 2 High, 3 High

    # compare hands
        # Assign a value to each type (Flush, Straight, etc)
        # create a 3-tuple for each hand
        # compare hand[0]
            # if needed, compare hand[1]
            # if needed, compare hand[2]

# straight flush = 100
# four kind = 90
# full house = 80
# flush = 70
# straight = 60
# 3Kind = 50
# Two Pair = 40
# Pair = 30
# Nothing = 0

import csv

wins_a = 0
wins_b = 0

with open('p054_poker.txt', newline='') as f:
    reader = csv.reader(f)
    
    data = list(reader)

f = open('p54_output.txt','w')

def evalofKind(hand):
    khand = []
    for i in range(0,5):
        pos = 3*i
        if hand[pos] =='T':
            khand.append(10)
        elif hand[pos] =='J':
            khand.append(11)
        elif hand[pos] =='Q':
            khand.append(12)
        elif hand[pos] =='K':
            khand.append(13)
        elif hand[pos] =='A':
            khand.append(14)
        else: khand.append(int(hand[pos]))
    khand.sort()
    if khand[0] == khand[3] or khand[1] == khand[4]:
        return 'Four of a Kind'
    if  khand[0] == khand[2] or khand[2] == khand[4]:
        return 'Three of a Kind'
    if (khand[0] == khand[1] and khand[2] == khand[3]) or \
        (khand[1] == khand[2] and khand[3] == khand[4]) or \
            (khand[0] == khand[1] and khand[3] == khand[4]):
            return 'Two Pair'
    for j in range(0,4):
        if khand[j] == khand[j+1]:
            return 'One Pair'
    return 'High Card'

def evalFullHouse(hand):
    fhand = []
    for i in range(0,5):
        pos = 3*i
        if hand[pos] =='T':
            fhand.append(10)
        elif hand[pos] =='J':
            fhand.append(11)
        elif hand[pos] =='Q':
            fhand.append(12)
        elif hand[pos] =='K':
            fhand.append(13)
        elif hand[pos] =='A':
            fhand.append(14)
        else: fhand.append(int(hand[pos]))
    fhand.sort()

    if (fhand[0]==fhand[2] and fhand[3]==fhand[4]) or \
        (fhand[0]==fhand[1] and fhand[2]==fhand[4]):
        return 'Full House'
    else: return 'Not Full House'



def evalFlush(hand):
    suit = []
    for i in range(0,5):
        suit_pos = 3*i+1
        if i == 0:
            suit.append(hand[suit_pos])
        else:
            if i > 0 and hand[suit_pos] == suit[0]:
                suit.append(hand[suit_pos])
            else: return 'Not Flush'
    return 'Flush'

def evalStraight(hand):
    strt = []
    for i in range(0,5):
        str_pos = 3*i
        if hand[str_pos] =='T':
            strt.append(10)
        elif hand[str_pos] =='J':
            strt.append(11)
        elif hand[str_pos] =='Q':
            strt.append(12)
        elif hand[str_pos] =='K':
            strt.append(13)
        elif hand[str_pos] =='A':
            strt.append(14)
        else: strt.append(int(hand[str_pos]))
    strt.sort()
    if strt[1] == strt[0]+1 and strt[2] == strt[0]+2 and strt[3] == strt[0]+3 and strt[4] == strt[0]+4:
        return 'Straight'
    else: return 'Not Straight'

# need to return 3 high cards [two pair and tie-breaker]
def highCard(hand,status):
    hhand = []
    
    for i in range(0,5):
        str_pos = 3*i
        if hand[str_pos] =='T':
            hhand.append(10)
        elif hand[str_pos] =='J':
            hhand.append(11)
        elif hand[str_pos] =='Q':
            hhand.append(12)
        elif hand[str_pos] =='K':
            hhand.append(13)
        elif hand[str_pos] =='A':
            hhand.append(14)
        else: hhand.append(int(hand[str_pos]))

    hhand.sort()

    if status[1] in ['Straight','Straight Flush']:
        return [hhand[4],hhand[3],hhand[2]]

    elif status[1] == 'Flush':
        return [hhand[4],hhand[3],hhand[2]]

    elif status[1] == 'Full House':
        if hhand[2] == hhand[0]:
            return [hhand[0],hhand[4],0]
        else: return [hhand[4],hhand[0],0]

    elif status[1] == 'Four of a Kind':
        if hhand[0]==hhand[1]:
            return [hhand[0],hhand[4],0]
        else: return[hhand[4],hhand[0],0]

    elif status[1] == 'Three of a Kind':
        if hhand[0] == hhand[2]:
            return [hhand[0],hhand[4],hhand[3]]
        elif hhand[1] == hhand[3]:
            return [hhand[2],hhand[4],hhand[0]]
        else: return [hhand[4],hhand[1],hhand[0]]

    elif status[1] == 'Two Pair':
        if hhand[4] == hhand[3] and hhand[2] == hhand[1]:
            return[hhand[4],hhand[2],hhand[0]]
        elif hhand[4] == hhand[3] and hhand[1] == hhand[0]:
            return [hhand[4],hhand[1],hhand[2]]
        else: 
            return[hhand[3],hhand[1],hhand[4]]
    

    elif status[1] == 'One Pair':
        if hhand[4]==hhand[3]:
            return [hhand[4],hhand[2],hhand[1]]
        elif hhand[3]==hhand[2]:
            return [hhand[3],hhand[4],hhand[1]]
        elif hhand[2] == hhand[1]:
            return [hhand[2],hhand[4],hhand[3]]
        else: return [hhand[1],hhand[4],hhand[3]]
    
    #high cards here
    else: return [hhand[4],hhand[3],hhand[2]]
    

def evalHand(hand):
    if evalFlush(hand)=='Flush' and evalStraight(hand) == 'Straight':
        return [100,'Straight Flush']
    if evalFlush(hand)=='Flush':
        return [70,'Flush']
    if evalStraight(hand)=='Straight':
        return [60,'Straight']
    if evalFullHouse(hand) == 'FullHouse':
        return [80,'Full House']
    kindHand = evalofKind(hand)
    if kindHand in ('Four of a Kind', 'Three of a Kind','Two Pair','One Pair'):
        if kindHand == 'Four of a Kind':
            return [90,'Four of a Kind']
        elif kindHand == 'Three of a Kind':
            return [50,'Three of a Kind'] 
        elif kindHand == 'Two Pair':
            return [40,'Two Pair']
        else: return [30,'One Pair']
    else: return [0,'High Card']

for d in data:
    hand1 = str(d)[2:16]
    hand2 = str(d)[17:31]

    handStatus1 = evalHand(hand1)
    handStatus2 = evalHand(hand2)


    high1 = highCard(hand1,handStatus1)
    high2 = highCard(hand2,handStatus2)

    if handStatus1 == handStatus2:
        f.write('Same type of hand.\n')
    else: f.write('Different type of hands.\n')

    
    print('Player A holds: {} | {} points, {}, {},{},{} high'.format(hand1,handStatus1[0],handStatus1[1],high1[0],high1[1],high1[2]))
    print('Player B holds: {} | {} points, {}, {},{},{} high'.format(hand2,handStatus2[0],handStatus2[1],high2[0],high2[1],high2[2]))

    f.write('Player A holds: {} | {} points, {}, {},{},{} high\n'.format(hand1,handStatus1[0],handStatus1[1],high1[0],high1[1],high1[2]))
    f.write('Player B holds: {} | {} points, {}, {},{},{} high\n'.format(hand2,handStatus2[0],handStatus2[1],high2[0],high2[1],high2[2]))

    if handStatus1[0]>handStatus2[0]:
        print('Player A wins')
        f.write('A Wins\n\n')
        wins_a += 1
    elif handStatus1[0]<handStatus2[0]:
        print('Player B wins')
        f.write('B Wins\n\n')
        wins_b += 1
    if handStatus1[0] == handStatus2[0]:
        if high1[0]>high2[0]:
            print('Player A wins')
            f.write('A Wins\n\n')
            wins_a += 1
        elif high1[0]<high2[0]:
            print('Player B wins')
            f.write('B Wins\n\n')
            wins_b += 1
        elif high1[1] > high2[1]:
            print('Player A wins')
            f.write('A Wins\n\n')
            wins_a += 1
        elif high1[1]<high2[1]:
            print('Player B wins')
            f.write('B Wins\n\n')
            wins_b += 1
        elif high1[2] > high2[2]:
            print('Player A wins')
            f.write('A Wins\n\n')
            wins_a += 1
        elif high1[2]<high2[2]:
            print('Player B wins')
            f.write('B Wins\n\n')
            wins_b += 1
        else: 
            print('No Winners')
            f.write('No one Wins\n\n')

    print('\n')

print('Player A won {} hands.'.format(wins_a))
print('Player B won {} hands.'.format(wins_b))

f.close()
