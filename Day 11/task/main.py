import random
import art

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_deal = random.choice(cards)
    return random_deal

def calculate_score(hand):
    score = sum(hand)
    cards_in_hand = len(hand)
    if cards_in_hand == 2 and score == 21:
        return 0
    while score > 21 and 11 in hand:
        score -= 10
    return score

def compare_score(players_score, pc_score):
    if players_score > 21:
        return "You went over. You lose 😭"
    if pc_score > 21:
        return "You win 😃"
    if players_score == 0:
        return "You win 😃"
    if pc_score == 0:
        return "You lose 😭"
    if players_score == pc_score:
        return "It's a draw"
    if players_score > pc_score:
        return "You win 😃"
    if players_score < pc_score:
        return "You lose 😭"
    return None


def blackjack():

    game_over = False

    while not game_over:

        start_menu = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

        if start_menu not in ("y", "n"):
            print("Invalid Input. Try again.")
            continue

        if start_menu == "y":
            players_hand = []
            pc_hand = []
            print(art.logo)
            """the loop repeats twice: it gives one card to the player and one card to the dealer."""
            for _ in range(2): # value is not important here, so throwaway variable '_' was used
                players_hand.append(deal_cards())
                pc_hand.append(deal_cards())

            players_score = calculate_score(players_hand)
            pc_score = calculate_score(pc_hand)

            if players_score == 0 or pc_score == 0:
                game_over = True

                pc_display_score = 21 if pc_score == 0 else pc_score
                players_display_score = 21 if players_score == 0 else players_score

                print(f"Your final hand: {players_hand}, final score: {players_display_score}")
                print(f"Computer's final hand: {pc_hand}, final score: {pc_display_score}")

                print(compare_score(players_score, pc_score))
                continue

            print(f"Your cards: {players_hand}, current score: {players_score}")
            print(f"Computer's first card: {pc_hand[0]}")

        elif start_menu == "n":
            game_over = True
            continue

        dealing_over = False

        while not dealing_over:

            get_card = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()

            if get_card not in ("y", "n"):
                print("Invalid Input. Try again.")
                continue

            if get_card == "y":
                players_hand.append(deal_cards())
                players_score = calculate_score(players_hand)
                pc_score = calculate_score(pc_hand)

                if players_score > 21:
                    dealing_over = True

                    pc_display_score = 21 if pc_score == 0 else pc_score
                    print(f"Your final hand: {players_hand}, final score: {players_score}")
                    print(f"Computer's final hand: {pc_hand}, final score: {pc_display_score}")

                    print(compare_score(players_score, pc_score))

                else:
                    print(f"Your cards: {players_hand}, current score: {players_score}")
                    print(f"Computer's first card: {pc_hand[0]}")

            elif get_card == "n":

                players_score = calculate_score(players_hand)
                pc_score = calculate_score(pc_hand)

                score_is_17 = False

                while not score_is_17:

                    if pc_score < 17:
                        pc_hand.append(deal_cards())
                        pc_score = calculate_score(pc_hand)
                    else:
                        dealing_over = True
                        score_is_17 = True

                    pc_display_score = 21 if pc_score == 0 else pc_score
                    players_display_score = 21 if players_score == 0 else players_score

                print(f"Your final hand: {players_hand}, final score: {players_display_score}")
                print(f"Computer's final hand: {pc_hand}, final score: {pc_display_score}")

                print(compare_score(players_score, pc_score))

blackjack()

