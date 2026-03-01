import art
import game_data
import random


def random_choice():
    random_dict = random.choice(game_data.data)
    return random_dict


def compare(u_choice, first_pick, second_pick):
    if u_choice == "a":
        return first_pick > second_pick
    if u_choice == "b":
        return second_pick > first_pick
    return None


def game():
    print(art.logo)
    game_over = False
    score = 0

    first_pick = random_choice()

    while not game_over:

        second_pick = random_choice()

        while first_pick == second_pick:
            second_pick = random_choice()

        print(f"Agent A: {first_pick['name']}, {first_pick['description']}, {first_pick['country']}")

        print(art.vs)

        print(f"Agent B: {second_pick['name']}, {second_pick['description']}, {second_pick['country']}")

        first_pick_value = first_pick['follower_count']
        second_pick_value = second_pick['follower_count']

        print(first_pick_value)
        print(second_pick_value)

        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        while player_choice not in ("a", "b"):
            print("Wrong input, please enter 'a' or 'b'")
            player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if compare(player_choice, first_pick_value, second_pick_value):
            score += 1
            first_pick = second_pick
            print(f"You're right! Current score {score}")
            print("\n" * 5)
        else:
            game_over = True
            print(f"Sorry, you lose. Final score {score}.")


game()
