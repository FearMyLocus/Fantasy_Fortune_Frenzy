import time
import random

playerIn = True
dealerIn = True
#players deck of cards
deck = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K',
    'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A'
]
playerHand = []
dealerHand = []
print('''
  , __  _              _                   _   
 /|/  \| |            | |  /\             | |  
  | __/| |  __,   __  | | |  |  __,   __  | |  
  |   \|/  /  |  /    |/_)|  | /  |  /    |/_) 
  |(__/|__/\_/|_/\___/| \_/\_|/\_/|_/\___/| \_/
                            /|                 
                            \|                 
by @FearMyLocus
''')
print('welcome to BlackJack...' )
time.sleep(0.4)
print("\nLet's begin...\n")


#deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


#figure out the total of hand
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(2, 11):
            total += card
        elif card in face:
            total += 10
        elif card == 'A':
            if total > 10:
                total += 1
        else:
            total += 11
        return total

        


#check the winner
def revealdealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]


#game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"dealer had {revealdealerHand()} and ???")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    if playerIn:
        stayOrHit = input('1: Stay\n2: hit\n')
    if total(dealerHand) > 21:
        dealerIn = False
    elif total(dealerHand) < 17:
        dealerIn = True
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerin = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(
        f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}"
    )
    print('blackjack!... ' + name + ' WON!!')
elif total(dealerHand) == 21:
    print(
        f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}"
    )
    print('BlackJack!... Dealer Wins!')
elif total(playerHand) > 21:
    print(
        f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}"
    )
    print(name + ' bust, Dealer Wins!')
elif total(dealerHand) > 21:
    print(
        f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}"
    )
    print('dealer busts...', name + ' won!')
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(
        f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}"
    )
    print('Dealer Wins!!!')
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(name + ' WIN!!!')
