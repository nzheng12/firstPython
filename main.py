

result = 24
name_of_unit = " hours"


def days_to_units(num_of_days_element):
    return str(num_of_days_element) + " days are " + str(num_of_days_element * result) + str(name_of_unit)


def validate_and_execute():
    if str(user_input).isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("value can't be 0")
    else:
        print("not valid")


user_input = ""
while user_input != "exit":
    user_input = raw_input("enter a number of days\n")
    for num_of_days_elements in (user_input.split()):
        validate_and_execute()
