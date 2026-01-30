"""
Rock Paper Scissors Game

A simple Python game where the player competes against the computer
using basic decision-making and randomization.
"""

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

game_images = [rock, paper, scissors]

print("What do you choose?")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors")

choice = int(input())

if choice < 0 or choice > 2:
    print("Invalid choice. You lose!")
else:
    print("Your choice:")
    print(game_images[choice])

    computer_choice = random.randint(0, 2)
    print("Computer choice:")
    print(game_images[computer_choice])

    if choice == computer_choice:
        print("It's a draw!")
    elif (choice == 0 and computer_choice == 2) or \
         (choice == 1 and computer_choice == 0) or \
         (choice == 2 and computer_choice == 1):
        print("🎉 You win!")
    else:
        print("😞 You lose!")
