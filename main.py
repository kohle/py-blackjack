# py-blackjack
# File description: Main class for the program
# Developed by Kohle Feeley
# Burlington, Vermont 2017

# Import Python classes
import random

# Import project classes
from deck import *
from math_functions import *

# Create the cards in the deck
# Since ace is either a 1 or 11 it is easier to go in JQKA order
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

# Method that deals 2 cards into a hand (a list), remove from deck
def deal(deck) :
    hand = []

    for x in range(2) :
        random.shuffle(deck)
        card = deck.pop()

        # If we pick a JQKA, change it from a number to a string for the list
        if card == 11 :
            card = "J"
        if card == 12 :
            card = "Q"
        if card == 13 :
            card = "K"
        if card == 14 :
            card = "A"

        hand.append(card)

    return hand

# Method to hit, adds another card to the specified hand
def hit(hand) :
    card = deck.pop()

    # If we pick a JQKA, change it from a number to a string for the list
    if card == 11 :
        card = "J"
    if card == 12 :
        card = "Q"
    if card == 13 :
        card = "K"
    if card == 14 :
        card = "A"

    hand.append(card)

    return hand


# Method to determime who won and print the appropriate statement
def winner() :
    if dealer_total > 21 :
        print("The dealer busted! You win!")
    elif player_total > 21 :
        print("You busted! Dealer wins!")
    elif dealer_total > player_total :
        print("Dealer wins!")
    elif player_total > dealer_total :
        print("Player wins!")
    elif player_total == dealer_total :
        print("It\'s a tie!")


# Smiple testing procedure; NOT a working game:
# Deal the house and the player
dealer = deal(deck)
player = deal(deck)

# Print the results
print("Dealer\'s hand:", str(dealer), "Total:", str(total(dealer)))
print("Player\'s hand:", str(player), "Total:", str(total(player)))

# Hit the player
player = hit(player)
print("Player\'s hand:", str(dealer), "Total:", str(total(dealer)))

# Get the totals
dealer_total = total(dealer)
player_total = total(player)

# Winner
winner()
