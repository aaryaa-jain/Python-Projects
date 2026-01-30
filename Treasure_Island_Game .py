"""
Treasure Island Game

A text-based adventure game where the player makes choices to navigate
through different scenarios in search of hidden treasure.
This project demonstrates the use of conditional statements and
user input handling in Python.
"""

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

choice = input("You're at a cross road. Where do you want to go?\nleft / right\n").strip().lower()

if choice == "left":
    choice1 = input("You've come to a lake.\nType wait to wait for a boat. Type swim to swim across.\n").strip().lower()

    if choice1 == "wait":
        choice2 = input(
            "You arrive at the island unharmed.\n"
            "There is a house with 3 doors: red, yellow, and blue.\n"
            "Which colour do you choose?\n"
        ).strip().lower()

        if choice2 == "red":
            print("🔥 Burned by fire. Game Over.")
        elif choice2 == "yellow":
            print("🎉 You won! Congratulations!")
        elif choice2 == "blue":
            print("🐺 Eaten by beasts. Game Over.")
        else:
            print("❌ Wrong choice. Game Over.")
    else:
        print("🦈 Attacked by sharks. Game Over.")
else:
    print("🕳️ Fell into a hole. Game Over.")
