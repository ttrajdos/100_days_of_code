import random

def hot():
    num = random.randint(0, 1)
    if num == 0:
        print("Heads")
    else:
        print("Tails")

hot()