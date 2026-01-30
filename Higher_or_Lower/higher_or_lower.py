"""
Higher or Lower: Follower Guessing Game

A console-based game where the player guesses which of two social media accounts
has more followers. The game continues until the player makes an incorrect guess,
with the score increasing for each correct answer.
"""

import random
import os
from art import logo, vs
from game_data import data

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Returns True if the user's guess is correct, False otherwise."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def higher_lower_game():
    """Main function to run the Higher or Lower game."""
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        # Make account B the next account A
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:  # Ensure no duplicate accounts
            account_b = random.choice(data)

        # Display formatted account data
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for their guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        print(logo)

        # Get follower counts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check answer and update score
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False

# Start the game
if __name__ == "__main__":
    higher_lower_game()
