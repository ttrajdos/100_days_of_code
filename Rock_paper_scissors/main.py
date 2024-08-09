import random
import heads_or_tails

hands = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

choices = ['rock', 'paper', 'scissors']

computer_choice = random.randint(0, 2)
# print(hands[computer_choice])
# print(choices[computer_choice])
computer_choice = 2

user_choice = input("What's your choice? Type \"rock\", \"paper\" or \"scissors\"\n")
if user_choice not in choices:
    print("Wrong input")
    exit(1)

uc = 0

if user_choice == "paper":
    uc = 1
elif user_choice == "scissors":
    uc = 2

print(f"computer chose\n{hands[computer_choice]}\n{choices[computer_choice]}")
print(f"you chose\n{hands[uc]}\n{choices[uc]}")

if computer_choice == uc:
    print("It's a draw")
elif computer_choice == 0:
    if uc == 1:
        print("you won")
    else:
        print("computer won")
elif computer_choice == 1:
    if uc == 2:
        print("you won")
    else:
        print("computer won")
else:
    if uc == 0:
        print("you won")
    else:
        print("computer won")

# heads_or_tails.hot()