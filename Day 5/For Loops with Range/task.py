# total = 0
# for number in range(1,101):
#     total += number
# print(total)
#
# for i in range(10, 0, -1):
#     print(i)

for num in range (1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)