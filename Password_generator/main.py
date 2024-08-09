import random

letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
digits = '1234567890'
special ='!@#$%^&*()_+=-/.,;][\<>?:{}|]'

letters_num = int(input("How many letters would you like to have in your pw?\n"))
digits_num = int(input("How many digits would you like to have in your pw?\n"))
special_num = int(input("How many special characters would you like to have in your pw?\n"))

out = []

for i in range(letters_num):
    out.append(letters[random.randint(0, len(letters)-1)])

for i in range(digits_num):
    out.append(digits[random.randint(0, len(digits)-1)])

for i in range(special_num):
    out.append(special[random.randint(0, len(special)-1)])

random.shuffle(out)

print(''.join(out))
