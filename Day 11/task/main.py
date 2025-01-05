import random

# BLACKJACK HOUSE RULES
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False

def player_turn():
    print(f"The dealers first card: {dealer[:1] + dealer[1 + 1:]}")
    # Allow player to draw another card or hold their current cards
    player_choice = input("Type 'y' to hit, and 'n' to hold: ").lower()
    if player_choice == "y":
        player.append(random.choice(deck))
        if sum(player) > 21 and 11 not in player:
            print(f"You busted. Your cards: {player}, Total: {sum(player)}")
            player_turn = False
            game_over = True
        elif sum(player) > 21 and 11 in player:
            for card in player:
                if card == 11:
                    card -= 10
                score_with_aces += card
            if score_with_aces <= 21:
                print(f"Your cards: {player}, current score: {score_with_aces}")
            else:
                print(f"You busted. Your cards: {player}, Total: {score_with_aces}")
                player_turn = False
                game_over = True
        else:
            print(f"Your cards: {player}, current score: {sum(player)}")

    elif player_choice == "n":
        print(f"Your cards: {player}, current score: {sum(player)}")
        player_turn = False
        dealer_turn = True

def dealer_turn():
    while sum(dealer) < 17 and sum(dealer) < sum(player) and sum(player) <= 21:
        dealer.append(random.choice(deck))

    print(f"Dealer's final hand: {dealer}, Total score: {sum(dealer)}")
    dealer_turn = False

while not game_over:
    player = []
    dealer = []
    player_turn = True
    dealer_turn = True
    score_with_aces = 0

    # Deal 2 cards to each player
    for card_number in range(0, 2):
        player.append(random.choice(deck))
        dealer.append(random.choice(deck))

    player_turn()
    dealer_turn()

    # Show the players cards and the dealers first card
    print(f"Your cards: {player}, current score: {sum(player)}")
    # print(f"The dealers first card: {dealer[:1] + dealer[1 + 1:]}")

    if sum(player) > 21 and sum(dealer) > 21:
        print("Tied Game")
    elif sum(player) > sum(dealer) and sum(player) <= 21 or sum(dealer) > 21:
        print("You Win")
    elif sum(player) < sum(dealer) and sum(dealer) <= 21 or sum(player) > 21:
        print("You Lose")
    elif sum(player) == sum(dealer):
        print("Tied Game")

    play_again = input("Do you want to play again? type 'y' or 'n'\n").lower()
    if play_again == "y":
        game_over = False
        print("\n" * 100)
    else:
        game_over = True


# player_turn = hit_or_hold(player_choice, player)
# game_over = did_bust(sum(player), player, player_turn)
