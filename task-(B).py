'''Create a program that asks the user to guess a number between 1-100.
The Program should then give hints to the user until they guess the current 
number in Python'''

import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

# Call the function
guess_number()
