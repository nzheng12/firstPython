import random

result = 24
name_of_unit = " hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return str(num_of_days) + " days are " + str(num_of_days * result) + str(name_of_unit)
    else:
        return "Must use positive numbers"


user_input = input("enter a number of days\n")
calculated_value = days_to_units(user_input)
print(calculated_value)