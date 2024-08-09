import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
         ]

def deal_card():
    picked_card = random.choice(cards)
    cards.remove(picked_card)
    return picked_card

def initalize():
    result = []
    result.append(deal_card())
    result.append(deal_card())
    
    return result

def total(cards):
    total = 0
    for card in cards:
        if card == 11 and total + card > 21:
            card = 1
        total += card
    
    return total

def print_cards(cards):
    print(f"{cards} -> {total(cards)}")
    return total(cards)

def user_turn(user_cards):

    while True:
        hit_or_stand = input("Type 'h' to hit and 's' to stand: ")
        user_score = total(user_cards)

        if hit_or_stand == "s":
            return user_score
        
        user_cards.append(deal_card())
        user_score = print_cards(user_cards)
        if user_score > 21:
            return user_score
        
def dealer_turn(dealer_cards, user_score):

    print_cards(dealer_cards)
    
    while True:
        print(f"Total is {total(dealer_cards)}")
        while (total(dealer_cards) < 17):
            dealer_cards.append(deal_card())
            print_cards(dealer_cards)
        
        dealer_score = total(dealer_cards)
        if dealer_score == 21:
            if user_score == dealer_cards:
                print("Tie")
            else:
                print("Dealer wins")
            return
    
        if dealer_score < 21:
            if dealer_score > user_score:
                print("Dealer wins")
                return 
            else:
                dealer_cards.append(deal_card())
                print_cards(dealer_cards)
                continue
        
        print("User wins")
        return


def blackjack():
    print(art.logo)

    user_cards = initalize()
    dealer_cards = initalize()

    print_cards(user_cards)
    if total(user_cards) == 21:
        print("Blackjack!")
        return
    print(f"[*, {dealer_cards[1]}]")

    user_score = user_turn(user_cards)
    if user_score > 21:
        print("Bust! You loose")
        return
    dealer_turn(dealer_cards, user_score)
            




while True:
    want_to_play = input("Do you want to play blackjack? (y/n)?: ")
    if want_to_play == "n":
        break
    blackjack()



