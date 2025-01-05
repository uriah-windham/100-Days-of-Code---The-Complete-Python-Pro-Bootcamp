import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# random_float = random.uniform(1, 10)
# print(random_float)

coin_flip = random.randint(=0 ,1)

player_choice = input("\"Heads\" or  \"Tails\"\n    ").lower()

if coin_flip == 0:
    coin_side = "Heads"
else:
    coin_side = "Tails"

if coin_side == "Heads":
    if player_choice == "heads":
        print("The coin is HEADS, you win.")

    elif player_choice == "tails":
        print("The coin is HEADS, try again.")

    else:
        print("Invalid choice. TRY AGAIN")

elif coin_side == "Tails":
    if player_choice == "tails":
        print("The coin is TAILS. you win.")

    elif player_choice == "heads":
        print("The coin is TAILS, try again.")

    else:
        print("Invalid choice. TRY AGAIN.")