import random

print(random.randint(1,6))  #random int between 1 and 6
print(random.uniform(0,1))  #between 0 and 1    0.159665
print(random.gauss(0,1))    #gaussian distribution
# Math game
"""First import random, get random int from range(1,10) both inclusive,get another rand. int from 1 to 10 inclusive
prompt the user for what the two integer multiplied is,print if correct or not, if correct print the right answer."""
import random
a=random.randint(1,10)
b=random.randint(1,10)
answer=input(f"What is {a} times {b}? ")
answer=int(answer)
if answer == a*b:
    print(f"Correct {a} times {b} is {answer}")
else:
    print(f"Incorrect {a} times {b} is {a*b}")

# Rock, Paper, Scissors Game

print("Enter choice: 1: Rock 2: Paper 3: Scissor")
choice=input("Choice (1/2/3): ")
choice=int(choice)

computer_choice = random.randint(1,3)
print(f"Computer: {computer_choice}")

if choice == computer_choice:
    print("Draw")
elif choice ==1:    # Rock
    if computer_choice == 2:    #Paper
        print("Computer wins")
    else:
        print("You win")
elif choice == 2:   # Paper
    if computer_choice == 1:    #Rock
        print("You win")
    else:
        print("Computer wins")
elif choice == 3:   # Scissors
    if computer_choice == 1:    #Rock
        print("Computer wins")
    else:
        print("You win")



