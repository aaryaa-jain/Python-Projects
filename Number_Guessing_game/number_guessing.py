"""
Number Guessing Game

A simple Python game where the player tries to guess a randomly chosen number
between 1 and 100. The player can select a difficulty level:
- Easy: 10 attempts
- Hard: 5 attempts

The game provides feedback if the guess is too high or too low and announces
the winner when guessed correctly.
"""

from random import randint
from art import logo

# Constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks the user's guess against the actual answer and returns remaining turns."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return turns  # Ensure turns is returned even if correct

def set_difficulty():
    """Sets the number of attempts based on chosen difficulty."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """Main function to run the Number Guessing Game."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate random number
    answer = randint(1, 100)
    # Uncomment the next line for debugging
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.\n")

# Start the game
if __name__ == "__main__":
    game()
