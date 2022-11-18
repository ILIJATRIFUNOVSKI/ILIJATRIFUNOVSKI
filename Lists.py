my_list = [ "Apple","Orange","Banana"]
print(my_list[0])   #accesing elements from list
print(my_list[-1])  #negative indexing
print(my_list.pop())    #remove and return last item from list
print(my_list)
my_list.append("Banana")    #appends object to the end of the list
another_list = ["France","Denmark","Sweden"]
new_list = my_list+another_list     # concatenation
print(new_list)

import random

print(random.choice(new_list))

random.shuffle(new_list)
print(new_list)

print(" ".join(new_list))

s = "awesome"
print("".join(random.sample(s,len(s))))

my_numbers = [3, 5, 2, 6, 8, 2]
print(max(my_numbers))
print(min(my_numbers))
print(sum(my_numbers))
print(len(my_numbers))
print(sum(my_numbers)/len(my_numbers))

# Jumbled Game
import random
words = ["father", "enterprise", "science", "programming", "resistance", "fiction", "condition", "reverse",
         "computer", "python"]
word = random.choice(words)
print(word)
jumble = "".join(random.sample(word, len(word)))
print(f"The jumble word is {jumble}.")
guess=input("Write your guess: ")
if guess==word:
    print("Correct")
else:
    print(f"Incorrect: The word is {word}")







