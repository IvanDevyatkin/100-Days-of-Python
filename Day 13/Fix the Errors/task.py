# code with a bug

# age = int(input("How old are you? "))
#
# if age > 18:
#     print("You can drive at age {age}.")

# fixed code

try:
    age = int(input("How old are you? "))
except ValueError:
    print("Wrong input. Use numbers such as 15.") # print why an error appeared
    age = int(input("How old are you? ")) # ask to input value again

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can't drive at age {age}.")
