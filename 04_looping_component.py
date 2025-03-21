# Functions go here

# Checks that users give a response
def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")


def get_ingredients():
    """Gets variable / fixed expenses and outputs
    panda (as a sting) and a subtotal of expenses"""

    # list for pandas
    all_ingredients = []

    # expenses dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("Ingredient needed: ")

        if item_name == "xxx":
            break

        all_ingredients.append(item_name)

    # return all items for now so we can check loop
    return all_ingredients

# Main Routine goes here


while True:
    item_name = not_blank("Ingredient needed: ")

    if item_name == "xxx":
        break
