# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])

# reproduced bug

# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6 # there is a bug because the list ends with the number 6
# print(dice_images[dice_num])

# fixed code

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])