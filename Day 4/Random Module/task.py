import random

coin_toss = random.randint(1, 2)
if coin_toss == 1:
    print("Heads")
elif coin_toss == 2:
    print("Tails")
else:
    print("Invalid choice. Try again.")