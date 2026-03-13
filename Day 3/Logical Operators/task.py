print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
free_ride: bool = False

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Child ticket costs ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth ticket costs ${bill}.")
    elif 45 <= age <= 55:
        print("Have a free ride on us!")
        free_ride = True
    else:
        bill = 12
        print(f"Adult ticket costs ${bill}.")

    if not free_ride:
        wants_photo = input("Would you like to see a photo of you? (y/n) ")
        if wants_photo == "y":
            bill += 3
        print(f"Your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
