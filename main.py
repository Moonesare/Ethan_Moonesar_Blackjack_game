#Import random to randomize and shuffle the deck
import random
#Set variables to handle if Player or Dealer is in
player_in = True
dealer_in = True

#deck of cards / player or delear hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4
player_hand = []
dealer_hand = []

#deal the cards
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    #Remove the card from the deck to prevent drawing it again
    deck.remove(card)

#calculate the total of each hand
def total(turn):
    total = 0
    # Track the number of Aces
    aces = 0
    face = ['J', 'Q', 'K']

#Set the value of face cards
    for card in turn:
        if card in face:
            #Face cards (J, Q, K) are worth 10
            total += 10
        elif card == 'A':
            #Aces handled after other cards
            aces += 1
        else:
            #Number cards retain their value
            total += card

    #Handle Aces after other cards
    for _ in range(aces):
        if total + 11 > 21:
            #Count Ace as 1 to avoid busting
            total += 1
        else:
            total += 1

    return total

#Check for winner
def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

#game loop
for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)

while player_in or dealer_in:
    #Show partial dealer hand and full player hand
    print (f"\nDealer has {reveal_dealer_hand()} and ?")
    print (f"You have {player_hand} for a total of {total(player_hand)}")
    #Player's decision
    if player_in:
        stay_or_hit = int(input("1: Stay \n2: Hit\nWhat will you do? (1 or 2): "))
        if stay_or_hit == 1:
            #Player stays
            player_in = False
        else:
            #Player hits
            deal_card(player_hand)

    #Dealer decision (must hit until reaching 17)
    if total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)

    #Break the loop if either busts or hits 21
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

#Determining the final results
#Player hand = 21
if total(player_hand) ==  21:
    print (f"\nYou have {player_hand} with a total of {total(player_hand)}.")
    print (f"The dealer has {dealer_hand} with a total of {total(dealer_hand)}.")
    print ("BLACKJACK! YOU WIN")
#Dealer hand = 21
elif total(dealer_hand) == 21:
    print(f"\nYou have {player_hand} with a total of {total(player_hand)}.")
    print(f"The dealer has {dealer_hand} with a total of {total(dealer_hand)}.")
    print ("AW! YOU LOST! NEVER GO TO VEGAS!")
#Dealer hand greater than 21
elif total(dealer_hand) > 21:
    print(f"\nYou have {player_hand} with a total of {total(player_hand)}.")
    print(f"The dealer has {dealer_hand} with a total of {total(dealer_hand)}.")
    print ("BLACKJACK! YOU WIN")
#Player hand greater than 21
elif total(player_hand) >  21:
    print (f"\nYou have {player_hand} with a total of {total(player_hand)}.")
    print (f"The dealer has {dealer_hand} with a total of {total(dealer_hand)}.")
    print ("AW! YOU LOST! NEVER GO TO VEGAS!")
#Player hand is higher than dealer hand
elif 21 - total(player_hand) < 21 - total(dealer_hand):
    print(f"\nYou have {player_hand} with a total of {total(player_hand)}.")
    print(f"The dealer has {dealer_hand} with a total of {total(dealer_hand)}.")
    print("BLACKJACK! YOU WIN")
#Dealer hand is higher than player hand
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"\nYou have {player_hand} with a total of {total(player_hand)}.")
    print(f"The dealer has {dealer_hand} with a total of {total(dealer_hand)}.")
    print("AW! YOU LOST! NEVER GO TO VEGAS!")
#Both hands are equal to each other
elif total(player_hand) == total(dealer_hand) and total(dealer_hand) == total(player_hand):
    print(f"\nYou have {player_hand} with a total of {total(player_hand)}.")
    print(f"The dealer has {dealer_hand} with a total of {total(dealer_hand)}.")
    print("IT'S A TIE!")