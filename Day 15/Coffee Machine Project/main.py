MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Todo create a calculator for inserted coins

def calculate_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# Todo create function that checks how many resources are left in Coffe Machine

def check_resources(drink_to_make):
    for item in drink_to_make:
        if resources[item] < drink_to_make[item]:
            print(f"Not enough {item} to make a drink")
            return False
    return True


def is_transaction_successful(drink_cost, inserted_coins):
    if drink_cost > inserted_coins:
        print("Not enough money to make a drink")
        return False
    else:
        global profit
        change = round(inserted_coins - drink_cost, 2)
        profit += change
        print(f"Here is your change: ${change}")
        return True


def make_coffee(drink_choice, ingredients_for_drink):
    for item in ingredients_for_drink:
        resources[item] -= ingredients_for_drink[item]
    print(f"Here is your {drink_choice}")


is_on = True

while is_on:
    choose_action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose_action == "off":
        is_on = False
        print("Machine is turning off")
    elif choose_action == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if choose_action not in MENU:
            print("Invalid choice. Please choose espresso, latte, or cappuccino.")
            continue
        drink = MENU[choose_action]
        if check_resources(drink["ingredients"]):
            payment = calculate_coins()
            if is_transaction_successful(drink["cost"], payment):
                make_coffee(choose_action, drink["ingredients"])
