# py-blackjack
# File description: Contains the functions that calculate values
# Developed by Kohle Feeley
# Burlington, Vermont 2017

# Method to calculate the hand's total value
def total(hand) :
    total = 0

    for card in hand :
        if card == "J" or card == "Q" or card == "K" :
            total = total + 10
        elif card == "A" :
            if total >= 11 :
                total = total + 1
            else :
                total = total + 11
        else :
            total = total + card

    return total
