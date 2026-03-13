import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")

EASY_LEVEL = 10
HARD_LEVEL = 5

def difficulty_level():
    level_hardness = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    while level_hardness not in ("easy", "hard"):
        print("Invalid Input. Try again.")
        level_hardness = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level_hardness == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def number_generator():
    generated_number = random.randint(1,100)
    return generated_number

def compare_numbers(u_number, c_number):
    if u_number == c_number:
        return "You win!"
    if u_number < c_number:
        return "Too low. Guess again."
    if u_number > c_number:
        return "Too high. Guess again."
    return None

def play_game():

    secret_number = number_generator()
    print(f"The correct number is {secret_number}.")
    print("I'm thinking of a number between 1 and 100.")
    attempts = difficulty_level()

    while attempts > 0:

        user_number = int(input("Make a guess: "))

        while user_number not in range(1,101):
            print("Please guess a number between 1 and 100.")
            user_number = int(input("Make a guess: "))

        if user_number == secret_number:
            print(f"You win! The answer was {secret_number}.")
            break

        attempts -= 1

        if attempts == 0:
            print(compare_numbers(user_number, secret_number))
            print("You've run out of guesses, you lose.")
            break

        else:
            print(compare_numbers(user_number, secret_number))
            print(f"You have {attempts} attempts remaining to guess the number.")

play_game()


