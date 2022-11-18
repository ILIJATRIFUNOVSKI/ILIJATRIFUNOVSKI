my_dict = {
    'Key1': 'Value1',
    'Key2': 'Value2'
}
print(my_dict['Key1'])

my_dict['Key3'] = 'Value3'
print(my_dict)

my_dict['Key2'] = 'Value3'  #updating
print(my_dict)

car = {
    'Brand': 'Lamborgini',
    'Model': 'Sian',
    'Year': 2022
}
print(car)

items = ["Pen", "Scissor", "Pen", "Pen", "Scissor"]
count={}
for item in items:
    count[item] = count.get(item,0) + 1
print(count)

for key, value in count.items():
    print(key, value)
for key, value in car.items():
    print(key, value)

print(car.keys())
print(list(car.keys()))
print(list(count.keys()))
print()

#Capitals and Frequency Count
import random

capitals = {'France': 'Paris', "Findland": "Helsinki", "Sweden": "Stockholm", "Denmark": "Copenhagen"}

score = 0

for i in range(3):
    country = random.choice(list(capitals.keys()))

    answer = input(f"What is the capital of {country} ? ")

    if answer.lower() == capitals[country].lower():
        print(f"Correct! The capital of {country} is {capitals[country]}!")
        score = score + 1
    else:
        print(f"Incorrect! The capital of {country} is {capitals[country]}!")

print(f"Your score: {score} ")
# Frequency Count
text = input("Write a line of text: ")

freq = {}
for c in text:
    c.lower()
    freq[c] = freq.get(c, 0) + 1

for key, value in freq.items():
    print(f"{key}: {value}")
