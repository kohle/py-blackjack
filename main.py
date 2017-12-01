# py-blackjack
# File description: Main class for the program
# Developed by Kohle Feeley
# Burlington, Vermont 2017

# Import Python classes
import random

# Score variable
score = 0

# Create score file if it doesn't exist with base score, otherwise get score
try :
    score_file = open("score.txt", "r")
    score = float(str(score_file.read()))
    score_file.close()
    
except FileNotFoundError:
    score_file = open("score.txt", "w")
    score_file.write("10")
    score = 100
    score_file.close()
    

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
        print("#     [P]LAY [S]CORE [A]BOUT    #")
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
            print("\n############[ SCORE ]############")
            print("YOUR SCORE IS: ", str(score))
            print() # Break line
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

            # Betting procedure
            print("\n###########[ BETTING ]##########")
            print("YOU WILL RECEIVE 1.5x YOUR BET IF YOU WIN THE ROUND.")
            print("YOUR SCORE IS: ", str(score))
            betting = input("DO YOU WANT TO PLACE A BET? (Y/N): ")
            amount = 0

            if betting.lower() == "y" :
                amount = input("ENTER YOUR BET: ")
                amount = float(str(amount))

                while amount > score :
                    print("YOU MUST ENTER AN AMOUNT LESS THAN YOUR SCORE.")
                    amount = input("ENTER YOUR BET: ")
                    amount = float(str(amount))

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

                if amount > 0 :
                    winnings = amount * 1.5
                    new_score = score + winnings
                    print("You won", str(amount * 1.5), "points!")
                    print("Your new score is", str(new_score))
                    score_file = open("score.txt", "w")
                    score_file.write(str(new_score))
                    score_file.close()
            elif total(player) > 21 :
                print("You busted! Dealer wins!")

                if amount > 0 :
                    new_score = score - amount
                    print("You lost", str(amount), "points!")
                    print("Your new score is", str(new_score))
                    score_file = open("score.txt", "w")
                    score_file.write(str(new_score))
                    score_file.close()
            elif total(dealer) > total(player) :
                print("Dealer wins!")

                if amount > 0 :
                    new_score = score - amount
                    print("You lost", str(amount), "points!")
                    print("Your new score is", str(new_score))
                    score_file = open("score.txt", "w")
                    score_file.write(str(new_score))
                    score_file.close()
            elif total(player) > total(dealer) :
                print("Player wins!")
                
                if amount > 0 :
                    winnings = amount * 1.5
                    new_score = score + winnings
                    print("You won", str(amount * 1.5), "points!")
                    print("Your new score is", str(new_score))
                    score_file = open("score.txt", "w")
                    score_file.write(str(new_score))
                    score_file.close()
            elif total(player) == total(dealer) :
                print("It\'s a tie!")

                if amount > 0 :
                    print("Nobody gets any points!")

            print() # Blank line

            break

game()
