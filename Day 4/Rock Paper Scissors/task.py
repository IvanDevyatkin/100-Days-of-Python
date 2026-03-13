import random
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_game_list = [rock, paper, scissors]

user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_move >= 0 and user_move <= 2:
    print(rps_game_list[user_move])

pc_index = random.randint(0, 2)
pc_move = rps_game_list[pc_index]

print("Computer chose: ")
print(pc_move)

if user_move >= 3 or user_move < 0:
    print("Invalid number. Try again.")
elif user_move == pc_index:
    print("It's a draw!")
elif user_move == 0 and pc_index == 2:
    print("You win!")
elif pc_index == 0 and user_move == 2:
    print("You lose!")
elif pc_index > user_move:
    print("You lose!")
elif user_move > pc_index:
    print("You win!")









