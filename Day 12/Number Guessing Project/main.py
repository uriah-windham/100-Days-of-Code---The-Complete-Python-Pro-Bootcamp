from random import randint
from art import logo

random_number = randint(1, 100)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def make_a_guess(correct_number, lives):
    print(f"You have {lives} attempts remaining to guess the number.")

    try:
        guess = int(input(f"\nMake a guess: "))
        if guess == correct_number:
            print(f"You got it! The answer was {correct_number}")
            return
        elif guess > correct_number:
            print("Too high.")
        elif guess < correct_number:
            print("Too Low.")
    except ValueError:
        print("That's not a number!")

    lives -= 1
    if lives == 0:
        print(f"You've run out of guesses. The correct number was {correct_number}.\n\nRefresh the page to play again.")
        return
    print("Guess Again")
    make_a_guess(correct_number, lives)

def set_difficulty(level):
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempts = set_difficulty(difficulty)
make_a_guess(random_number, attempts)