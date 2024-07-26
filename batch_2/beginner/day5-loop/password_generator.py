print("Welcome to PyPassword Generator")
password_length = int(input("How many letters would you like in your password?\n"))
password_symbol = int(input("How many symbols would you like?\n"))
password_number = int(input("How many numbers would you like?\n"))
password = ""
import random
for i in range(password_length):
    password += random.choice("abcdefghijklmnopqrstuvwxyz")
for i in range(password_symbol):
    password += random.choice("!@#$%^&*()")
for i in range(password_number):
    password += random.choice("1234567890")
# randomize order
password = ''.join(random.sample(password, len(password)))
print(password)
