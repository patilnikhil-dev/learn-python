import random

cards = ["jack", "queen", "king"]

print(f"original cards : {cards}")

random.shuffle(cards)

print("shuffled cards : ")
for card in cards:
    print(" ",card)
