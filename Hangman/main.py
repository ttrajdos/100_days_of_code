word_list = ["ardvark", "baboon", "camel"]

import random
import hangman_art


def verify_if_letter_is_in_string(guess, chosen_word, display, lives):
    if guess in chosen_word:
        for id, letter in enumerate(chosen_word):
            if guess == letter:
                display[id] = letter
        # print(' '.join(display))
    else:
        # print(' '.join(display))
        return False
    
def chooseWord(infile_name):
	infile = open(infile_name, 'r')
	wordlist = infile.readlines()
	total_words = len(wordlist)
	random_num = random.randint(0, total_words - 1)

	chosen_word = wordlist[random_num].replace('\n', '')
	return chosen_word

def main():
    print(hangman_art.logo)
    
    chosen_word = chooseWord("hangman_words.txt")

    number_of_lives = 7

    display = []
    for _ in chosen_word:
        display.append("_")

    guessed_letters = []

    while("_" in display):
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'")
            continue
        else:
            guessed_letters.append(guess)
        if verify_if_letter_is_in_string(guess, chosen_word, display, number_of_lives) == False:
            print(hangman_art.HANGMANPICS[len(hangman_art.HANGMANPICS)-number_of_lives])
            number_of_lives = number_of_lives - 1
            if number_of_lives == 0:
                print("You lost!")
                print(f"The word was {chosen_word}")
                return 0
        print(' '.join(display))
    print("You win!")

main()