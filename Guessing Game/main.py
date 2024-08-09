import random
import art

def get_number_of_attemps(difficulty):
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    return attempts
    

def guess(attempts, goal):
    while True:
        guess = int(input("Make a guess: "))
        if guess == goal:
            print(f"Correct! The number was {goal}")
            break
        elif guess > goal:
            print("Too high.")
        elif guess < goal:
            print("Too low.")
            
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you loose")
            break
        print(f"You have {attempts} attemps remaining to guess the number")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 an 100.")

number = int(random.randint(1, 100))
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")

attempts = get_number_of_attemps(difficulty)

guess(attempts, number)




