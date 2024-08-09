import art

alphabet = ([*"abcdefghijklmnopqrstuvwxyz"])

def caesar(text, shift, direction):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    cipher_text = ""
    if direction == "encode":
        for i in text:
            if i in alphabet:
                index = alphabet.index(i)
                cipher_text += shifted_alphabet[index]
            else:
                cipher_text += i
    else:
        for i in text:
            if i in shifted_alphabet:
                index = shifted_alphabet.index(i)
                cipher_text += alphabet[index]
            else:
                cipher_text += i

    print(f"The {direction}d text is '{cipher_text}'")


print(art.logo)

while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)

    caesar(text, shift, direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again != "yes":
        break
