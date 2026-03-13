# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# fixed code

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()



# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?

# 'i' is going through numbers from 1 to 19

# 2. When is the function meant to print "You got it"?

# never, because the loop stops on the number 19

# 3. What are your assumptions about the value of i?

# It will never be 20, so the condition i == 20 can never be true.