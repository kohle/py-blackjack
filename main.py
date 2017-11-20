# py-blackjack
# File description: Main class for the program
# Developed by Kohle Feeley
# Burlington, Vermont 2017

# Import Python classes
import random

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

playing = input("Would you like to play? (Y/N) ")

while playing.lower() == "y" :

    dealer = deal(deck)
    player = deal(deck)

    print("Dealer\'s hand:", str(dealer), "Total:", str(total(dealer)))
    print("Player\'s hand:", str(player), "Total:", str(total(player)))

    should_hit = input("Would you like to hit? (Y/N) ")

    while should_hit.lower() == "y" :
        player = hit(player)
        print("Player\'s hand:", str(dealer), "Total:", str(total(dealer)))

        if total(player) > 21 :
            print("You busted!")
            playing = input("Would you like to play? (Y/N) ")

        else :
            should_hit = input("Would you like to hit? (Y/N) ")

    # Get the totals
    dealer_total = total(dealer)
    player_total = total(player)

    # Winner
    winner()

    playing = input("Would you like to play? (Y/N) ")

else :
    print("Thanks for playing!")
