print("Welcome to number guessing game")
print ("I'm thinking of a number between 1 and 100")
import random
number = random.randint(1,100)
# print(f"Psst the number is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number")
guess = 0
while guess != number and attempts > 0:
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print(f"You got it! The number was {number}")
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
    else:
        print("You've run out of guesses, you lose")
        break

