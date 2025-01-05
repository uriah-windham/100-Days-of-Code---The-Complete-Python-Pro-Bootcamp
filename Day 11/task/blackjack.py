import random
import art

#Deck of cards
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_over = False
continue_game = True

# Gives the player the option to draw another card of hold their cards
def player_turn(player_cards):
    choice = input("\nType 'y' to draw another card or 'n' to hold: ").lower()
    print("")
    if choice == "y": #If the player draws, this adds a card to their hand and displays their new hand and total score
        player_cards.append(random.choice(deck))
        return True
    elif choice == "n": #If the player holds, this end their turn and passed it to the dealer's turn
        dealer_turn(dealer_hand)
        return False

#Has the dealer draw cards until their total score is at least 17
def dealer_turn(dealer_cards):
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(deck))

#Displays both players current hand and total score
def current_score(player_cards, dealer_cards):
    print(f"    Your cards: {player_cards}, Total score: {sum(player_cards)}")
    print(f"    The dealer's cards: {dealer_cards}, Total score: {sum(dealer_cards)}")

#Checks if a players hand exceed a total of 21
def did_bust(hand):
    for card in range(len(hand)): #if an 'Ace' is held in hand and the players hand goes over 21, this changes the 'Aces' value from 11 to 1
        if hand[card] == 11 and sum(hand) > 21:
            hand[card] = 1

    if sum(hand) > 21:
        return True
    else:
        return False

while not game_over:
    game_result = ""

    print(art.logo)

    #Generates both players starting hands
    player_hand = []
    dealer_hand = []
    for card_amount in range(0, 2):
        player_hand.append(random.choice(deck))
        dealer_hand.append(random.choice(deck))

    print(f"    Your cards: {player_hand}, Total score: {sum(player_hand)}")
    print(f"    The dealer's first card: {dealer_hand[0]}") #Only show the dealers first card in hand

    while continue_game:
        if player_turn(player_hand):
            continue_game = True
        else:
            continue_game = False

        if did_bust(player_hand) and did_bust(dealer_hand): #If both player bust, ties the game
            game_result = "Tied"
            continue_game = False
        elif did_bust(player_hand): #If player busts, they lose
            game_result = "Lose"
            continue_game = False
        elif did_bust(dealer_hand): #If dealer busts, player wins
            game_result = "Win"
            continue_game = False
        #If neither player busts - Checks you has to higher score total
        elif sum(player_hand) == sum(dealer_hand):
            game_result = "Tied"
        elif sum(player_hand) > sum(dealer_hand):
            game_result = "Win"
        elif sum(player_hand) < sum(dealer_hand):
            game_result = "Lose"

        if continue_game:
            print(f"    Your cards: {player_hand}, Total score: {sum(player_hand)}")
            print(f"    The dealer's first card: {dealer_hand[0]}")  # Only show the dealers first card in hand
        else:
            current_score(player_hand, dealer_hand)

    if sum(player_hand) > 21 and sum(dealer_hand) > 21:
        print("    Both players busted!")
    elif sum(player_hand) > 21:
        print("    You Busted!")
    elif sum(dealer_hand) > 21:
        print("    The dealer busted!")

    print(f"***************************YOU {game_result.upper()}***************************")

    #Restarts the game if player wants to play again
    play_again = input("\nType 'y' to play again, or 'n' to end game: ")
    if play_again == "y":
        continue_game = True
        print("\n" *100)
    else:
        game_over = True
        print("Come Again!")