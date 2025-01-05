import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_types = [rock, paper, scissors]

while True:
    bot_choice = random.choice(hand_types)

    print("Rock, Paper, or Scissors?")
    while True:
        try:
            player_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n    "))
            break

        except ValueError:
            print("Invalid choice: Disqualified!")
            break

    if player_choice >= 0 and player_choice < 3:
        print(f"You chose: {hand_types[player_choice]}")
        print(f"Computer chose: {bot_choice}")

    if player_choice == 0:
        if bot_choice == rock:
            print("You Tied")

        elif bot_choice == paper:
            print("You Lose")

        elif bot_choice == scissors:
            print("You Win")

    elif player_choice == 1:
        if bot_choice == rock:
            print("You Win")

        elif bot_choice == paper:
            print("You Tied")

        elif bot_choice == scissors:
            print("You Lose")

    elif player_choice == 2:
        if bot_choice == rock:
            print("You Lose")

        elif bot_choice == paper:
            print("You Win")

        elif bot_choice == scissors:
            print("You Tied")

    else:
        print("Invalid choice: Disqualified!")

    play_again = input("Do you want to play again? \"Y\" or \"N\"\n    ").lower()

    if play_again == "y":
        continue

    else:
        break