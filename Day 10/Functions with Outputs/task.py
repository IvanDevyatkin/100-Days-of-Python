# def format_name(first_name, last_name):
#     return first_name.title(), last_name.title()
#
# f_name = input("What is your first name?: ")
# l_name = input("What is your last name?: ")
#
# f_name, l_name = format_name(f_name, l_name)
#
# print(f_name, l_name)

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# print(is_leap_year(1989))

# def is_leap_year(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True
#
# print(is_leap_year(2020))

# def is_leap_year(year):
#     # Check 1: If this is true, return False and EXIT
#     if year % 4 != 0:
#         return False  # Function ends here
#
#     # If we reach here, year % 4 == 0 (check 1 was False)
#
#     # Check 2: If this is true, return True and EXIT
#     if year % 100 != 0:
#         return True  # Function ends here
#
#     # If we reach here, year % 100 == 0 (check 2 was False)
#
#     # Check 3: If this is true, return False and EXIT
#     if year % 400 != 0:
#         return False  # Function ends here
#
#     # If we reach here, year % 400 == 0 (check 3 was False)
#
#     # Default: only reached if all checks failed to return
#     return True  # This is the "catch-all" case

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(1989))

