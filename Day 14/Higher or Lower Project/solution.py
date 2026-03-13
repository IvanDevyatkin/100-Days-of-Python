# Display art
from art import logo, vs
from game_data import data
import random
import os


def clear_screen():
    """Clears the terminal screen."""
    os.system("clear")


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


def pick_random(exclude):
    """Pick a random account from data, avoiding any in the exclude set."""
    available = [account for account in data if account["name"] not in exclude]
    if not available:
        # All accounts used — reset the pool but still avoid the immediate exclude
        available = [account for account in data if account["name"] != exclude]
    return random.choice(available)


print(logo)
score = 0
game_should_continue = True
seen = set()

# Generate a random account from the game data.
account_b = random.choice(data)
seen.add(account_b["name"])

# Make the game repeatable.
while game_should_continue:

    # Making account at position B become the next account at position A.
    account_a = account_b

    # Pick a new B that is different from A, avoiding recently seen accounts.
    account_b = pick_random(seen)
    seen.add(account_b["name"])

    # Reset pool when most accounts have been seen.
    if len(seen) >= len(data) - 1:
        seen = {account_a["name"], account_b["name"]}

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    clear_screen()
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False


