#Boolean expressions (equal to,less than,greater than or equal to...)
a=10
b=12
if a==b:
    print("a equals b")
if a<b:
    print("a is less than b")

if a>b:
    print("a is greater than b")
else:
    print('a is not greater than b')
a=10
b=12
if a > b:
    print("a is greater than b")
elif a==b:
    print("a is equal than b")
else:
    print("a is less than b")
a =10
b = 12
if a != b:
    print("a does not equal b")
# PROJECT - Car Ensurance
#goal car ensurance calculation based on the following decision tree (7:38 youtube pic.)
gender=input("What is your gender (M/F): ")
gender=gender.upper()
if gender == "M":
    print("Male")
    age = input("What is your age? ")
    age = int(age)
    if age <= 26:
        print("Less equal to 26")
        percentage = 23
    else:
        print("More than 26")
        percentage = 9
elif gender == "F":
    print("Female")
    car_type = input("What is your car type (sports/non-sports) ")
    car_type = car_type.upper()
    if car_type == "SPORTS":
        print("Sports car")
        percentage = 21
    else:
        print("Non-sports car")
        percentage = 10
else:
    print("Wrong format")
    percentage = None

market_price = input("What is the market price of your car? ")
market_price = int(market_price)
ensurance_offer = market_price*percentage/100

print(f"Ensurance offer: {ensurance_offer}")




