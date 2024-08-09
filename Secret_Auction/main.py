import art
import os

def find_highest_bidder(bidders):
    """
    Takes bidders map (name: bid) and returns the one with the highest bid
    """
    print(bidders)
    highest_bid = 0
    highest_bidder = ""

    for k, v in bidders.items():

        if v > highest_bid:
            highest_bid = v
            highest_bidder = k

    return highest_bidder

print(art.gavel)
bidders = {}


while True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    bidders[name] = bid
    next_person = input("Is there another person (yes/no)?\n")

    if next_person == "no":
        break

    os.system('clear')

print(f"The winner is {find_highest_bidder(bidders)}")
