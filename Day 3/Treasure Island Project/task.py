print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("'left' or 'right'? ").lower().strip()

if direction == "left":
    movement = input("Choose 'swim' to swim to the island or 'wait' to wait for a boat? ").lower().strip()
    print(movement)
    if movement == "wait":
        door_choice = input("Which door? 'red', 'blue' or 'yellow' ").lower().strip()
        print(door_choice)
        if door_choice == "yellow":
            print("You win!")
        elif door_choice == "blue":
            print("You were eaten by beasts. Game Over.")
        elif door_choice == "red":
            print("You were burned by fire. Game Over.")
        else:
            print("That door does not exist. Game Over.")
    elif movement == "swim":
        print("You were attacked by trout. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif direction == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Wrong direction. Game Over.")