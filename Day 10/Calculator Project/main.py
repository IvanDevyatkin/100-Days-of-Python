import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return None
    return n1 / n2

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    print(art.logo)

    calculation_complete = False

    number1_choice = float(input("What is the first number?: "))

    while not calculation_complete:

        for operator in operations_dict:
            print(operator)

        operation_choice = input("Pick an operation: ")

        if operation_choice not in operations_dict:
            print("Invalid operation. Pick a valid operation from the following options: ")
            continue # jump back to loop start (skip everything below)

        number2_choice = float(input("What is the next number?: "))

        exec_operation = operations_dict[operation_choice]
        result = exec_operation(number1_choice, number2_choice)

        print(f"Result: {number1_choice} {operation_choice} {number2_choice} = {result}")

        correct_input = False

        while not correct_input:
            next_step = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation "
                              f"or type 'q' to quit: ").lower()

            if next_step not in ("y", "n", "q"):
                print("Invalid input. Try again.")
                continue

            correct_input = True

            if next_step == "y":
                number1_choice = result
            elif next_step == "n":
                number1_choice = float(input("What is the first number?: "))
            elif next_step == "q":
                calculation_complete = True
                print("Goodbye")

calculator()