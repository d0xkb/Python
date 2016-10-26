import random

deck = list('234567890JQKA' * 4)

value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       '0': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

summ = 0
while summ < 21:
    print('You have now', summ)
    q = input('Another card ')
    if q == 'yes':
        random.shuffle(deck)
        card = value[deck.pop()]
        print('You flipped', card)
        summ = summ + card
    elif q == 'no':
        break
    else:
        print('yes/no only')

if summ == 21:
    print('You win')
elif summ > 21:
    print('You lost.', summ, 'is too much')
else:
    print('You almost did it', 21 - summ, 'remains')
