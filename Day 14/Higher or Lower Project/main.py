import random
from game_data import data
import art


def more_followers(option_1, option_2):
    """Determines which option has more instagram followers"""
    if option_1["follower_count"] > option_2["follower_count"]:
        return option_1
    else:
        return option_2

def generate_option():
    """Generates a random option A or B"""
    return random.choice(data)

def check_user_answer(option_1, option_2, correct_answer, user_answer):
    """Check the user's answer to the correct answer and returns True or False"""
    if user_answer == "y" and correct_answer == option_2:
        return True
    elif user_answer == "n" and correct_answer == option_1:
        return True
    else:
        return False

game_continues = True
score = 0
print(art.logo)

option_a = generate_option()

while game_continues:
    option_b = generate_option()

    #Checks both generates options and ensures they are not the same and do not have the same follower count
    while option_a == option_b or option_a["follower_count"] == option_b["follower_count"]:
        option_b = generate_option()

    answer = more_followers(option_a, option_b)

    print(f"{option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(art.vs)
    print(f"\n{option_b['name']}, a {option_b['description']}, from {option_b['country']}.\n")

    print(f"Does {option_b['name']} have more or less Instagram followers than {option_a['name']}")
    user_guess = input("    Type 'y' for more or 'n' for less: ").lower()

    result = (check_user_answer(option_a, option_b, answer, user_guess))

    if result:
        print("\n" * 100)
        print(art.logo)
        score += 1
        print(f"You're right! Current Score: {score}.")
        option_a = option_b
    else:
        print("\n" * 100)
        print(art.logo)
        print(f"Sorry, that's wrong. Final Score: {score}.")
        game_continues = False