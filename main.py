# py-blackjack
# File description: Main class for the program
# Developed by Kohle Feeley
# Burlington, Vermont 2017

# Import Python classes
import random

# Create the deck of cards
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
    dealer_total = total(dealer)
    player_total = total(player)
    
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

# Game function that allows it to keep looping using break/while statements
def game() :
    while True:
        # Print main menu
        print("##########[ BLACKJACK ]##########")
        print("#                               #")
        print("#           MAIN MENU           #")
        print("#    [P]LAY [S]CORES [A]BOUT    #")
        print("#                               #")
        print("#################################")

        # Ask for user's input
        menu_choice = input("     ENTER YOUR CHOICE: ")

        # About screen
        while menu_choice.lower() == "a" :
            print("\n############[ ABOUT ]############")
            print("#                               #")
            print("#   Developed by Kohle Feeley   #")
            print("#           (C) 2017            #")
            print("#                               #")
            print("#################################\n")
            break

        # High score table
        while menu_choice.lower() == "s" :
            print("\nFUTURE SCORES\n")
            break

        # Actually playing the game
        while menu_choice.lower() == "p" :
            # Re-state the deck of cards to prevent it from running out if
            # the player decides to do multiple rounds
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

            # Create the two hands
            dealer = deal(deck)
            player = deal(deck)

            # Tell the players their current total
            print("\n############[ HAND ]############")
            print("YOUR HAND:", str(player))
            print("YOUR TOTAL:", str(total(player)))

            # Ask if they want to hit
            hit_hand = input("\nDO YOU WANT TO HIT? (Y/N): ")

            # If they want to hit
            if hit_hand.lower() == "y" :
                hit(player)

                # Give them their new hand
                print("\n############[ HAND ]############")
                print("YOUR HAND:", str(player))
                print("YOUR TOTAL:", str(total(player)))

                # If the player didn't bust
                if total(player) < 21 :
                    # This is the cut-off I decided for the dealer hitting
                    if total(dealer) < 12 :
                        hit(dealer)

            print("\n###########[ RESULTS ]##########")
            print("YOUR TOTAL:", str(total(player)))
            print("DEALER TOTAL:", str(total(dealer)))
            print() # Blank line
            
            if total(dealer) > 21 :
                print("The dealer busted! You win!")
            elif total(player) > 21 :
                print("You busted! Dealer wins!")
            elif total(dealer) > total(player) :
                print("Dealer wins!")
            elif total(player) > total(dealer) :
                print("Player wins!")
            elif total(player) == total(dealer) :
                print("It\'s a tie!")

            print() # Blank line

            break



            
        

game()
