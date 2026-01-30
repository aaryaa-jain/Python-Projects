"""
Silent Auction Program:

A simple Python program that allows multiple users to place bids in a silent auction.
The program records each bidder's name and bid amount, then determines and announces
the highest bidder at the end. Easy-to-use console interface.
"""

from art import logo
import os

# Print the auction logo
print(logo)

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    """Determines and prints the highest bidder from the bidding record."""
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Main auction loop
bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        clear_screen()
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()
