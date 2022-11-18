def my_func():
    print("Hello, World!")
my_func()

def print_name(name):
    print(f"Hello, {name}")
print_name("Ilija")
print_name("Rune")

def print_age(name, age):
    print(f"Hello {name}")
    print(f"You are {age} years old")
print_age("Ilija", 28)

def calculate_age(birth_year):
    return 2022 - birth_year
    print("HELLO")  #we have return does not execute
calculate_age(1994)

# New things
print(ord("A")) #order of unicode for character
print(ord("B"))
print(chr(65))
print(chr(66))

for c in range(65, 65+26):
    print(f"{c} is {chr(c)}")   #printing the alphabet
hours=50    # 24 hour clock counting the hours
print(hours % 24)

def is_even(n):
    if n % 2 ==0:
        print("even")
    else:
        print("Odd")
is_even(1)

for i in range(10):
    print(i, end=" ")
    is_even(i)

# Caesar Cipher
def encrypt_char(char, key):
    return chr(ord("A") + (ord(char) - ord("A") + key) % 26)
print(encrypt_char("Z", 3))
def encrypt_message(message, key):
    message = message.upper()
    cipher =""
    for c in message:
        if c in " .,":
            cipher = cipher + c
        else:
            cipher = cipher + encrypt_char(c, key)
    return cipher
print(encrypt_message("you are awesome", 3))
def decrypt_char(char, key):
    return chr(ord("A") + (ord(char) - ord("A") + 26 - key) % 26)
def decrypt_message(cipher, key):
    message=""
    for c in cipher:
        if c in " .,":
            message= message + c
        else:
            message = message + decrypt_char(c, key)
    return message
print(decrypt_message("BRX DUH DZHVRPH", 3))

def decrypt_message2(cipher, key):
    return encrypt_message(cipher, 26 - key)
print(decrypt_message2("BRX DUH DZHVRPH", 3))

