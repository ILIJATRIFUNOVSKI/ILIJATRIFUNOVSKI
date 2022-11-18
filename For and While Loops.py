my_list = ["First", "Second", "Third"]
for item in my_list: #iterating over list
    print(item)

s="Ilija"
for c in s:
    print(c)
    print("Inside loop")
print("Outside the loop")

for i in range(2,4):
    print(i)

for i in range(len(my_list)):
    print(i,my_list[i])

value=10
while value > 0:
    value = int(input("Value? "))

s= "abc"
c="a"
if c in s:
    print("c is in s")

if c not in s:
    print("c is not in s")

a = 13
b = 12
c = 14
if a < b and b < c:
    print("awesome")
if a < b or b < c:
    print("awesome")

# Hangman Game

import random
words = ["father", "enterprise", "science", "programming", "resistance", "fiction", "condition", "reverse",
         "computer", "python"]
word = random.choice(words)
guesses = ""
turns = 10
while turns > 0:
    print(f"You have {turns} turns left")
    guessed_all = True
    for c in word:
        if c in guesses:
            print(c, end=" ")
        else:
            print("_", end=" ")
            guessed_all = False
    print()
    if not guessed_all:
        guess = input("Guess a character: ")
        guesses = guesses+ guess
        if guess not in word:
            turns = turns-1
    else:
        turns = 0



