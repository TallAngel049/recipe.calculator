unit_map = {
    "kilogram": "kg",
    "kilograms": "kg",
    "kg": "kg"
}

# Functions go here


def string_check(question, valid_ans):
    """check that users enter the correct unit"""

    while True:
        response = input(question).lower()

        # checks user response
        if response in valid_ans:
            return valid_ans[response]

        else:
            print(f"Please choose a valid option eg 'kg'.")


test = string_check("Enter a unit ", unit_map)
print(f"You chose {test}")
