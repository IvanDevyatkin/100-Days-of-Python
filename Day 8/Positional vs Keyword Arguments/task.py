# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# def name_and_age(name, age):
#     print(f"My name is {name} and my age is {age}")
#
# name_and_age("Ivan", 31)

# def greet_with(name, location):
#     print(f"Hello {name}!\nWhat is like in {location}?")
#
# # greet_with("Ivan", "Prague")
#
# greet_with(location="Prague", name="Ivan" )

# word_true = "true"
# word_love = "love"
#
# def calculate_love_score(name1, name2):
#     true_letters_list = []
#     love_letters_list = []
#
#     combined_names = (name1 + name2).lower()
#
#     for letter in combined_names:
#         if letter in word_true:
#             true_letters_list.append(letter)
#         if letter in word_love:
#             love_letters_list.append(letter)
#
#     true_len = len(true_letters_list)
#     love_len = len(love_letters_list)
#
#     print(f"love score: {true_len}{love_len}")
#
# calculate_love_score("Kanye West", "Kim Kardashian")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))

    print(f"Love score is: {score}")

calculate_love_score("Ivan", "Kristina")