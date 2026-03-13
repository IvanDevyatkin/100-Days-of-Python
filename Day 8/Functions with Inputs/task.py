def greet():
    print("Hello")
    print("My")
    print("friend!")

greet()


def life_in_weeks(age):
    year_in_weeks = 52
    weeks_left_to_live = (90 - age) * year_in_weeks
    print(f"You have {weeks_left_to_live} weeks left.")


life_in_weeks(56)