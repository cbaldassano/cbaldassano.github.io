def CardValue(card):
    if (card == 'J' or card == 'Q' or card == 'K'):
        return 10
    elif (card == 'A'):
        return 11
    else:
        return int(card)

card1 = input('Card 1: ')
card2 = input('Card 2: ')
card3 = input('Card 3: ')

handvalue = CardValue(card1) + CardValue(card2) + CardValue(card3)

# Need to add something here to deal with aces

# Need to add something here to determine whether to print "Bust"

print(handvalue)
