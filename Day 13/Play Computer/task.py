year = int(input("What's your year of birth?"))
#
# the code with a bug: when we input the year 1994, nothing happened

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

if year > 1980 and year <= 1994: # to include year '1994' we need to add '=' into condition
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

