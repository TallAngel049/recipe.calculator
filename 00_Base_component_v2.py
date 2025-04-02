# from datetime import date
# import pandas
# from tabulate import tabulate

# functions goes here


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # is the response is blank, output error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


def make_statement(statement, decoration):
    """Emphasises headings by adding
    decoration at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # check user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''

**** Instructions ****

This program will ask for...
- The name of your recipe
- The serving size needed for the recipe

Then the program will ask you to list the ingredients 
needed for your recipe, the amount and the unit. After which
the program will ask you to give the price, the amount and the unit.

The program outputs an itemised list of the amount, unit
and cost (which includes the cost per serving).

The data will also be write to a text file which has
the same name name as your recipe and the date. 

        ''')


def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:

        response = input(question)

        # check for exit code and return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_ingredients():
    """Gets variable / fixed expenses and outputs
    panda (as a sting) and a subtotal of expenses"""

    # list for pandas
    all_ingredients = []
    all_amounts = []
    all_units = []
    all_cost = []

    # expenses dictionary
    recipe_dict = {
        "Ingredients": all_ingredients,
        "Amount": all_amounts,
        "Unit": all_units,
        "Cost": all_cost
    }

    # loop to get expenses
    while True:
        item_name = not_blank("Ingredient needed: ")

        if item_name == "xxx":
            break

        all_ingredients.append(item_name)

    # return all items for now so we can check loop
    return all_ingredients


def string_check(question, valid_answers=("kg", "g", "ml", "l")):
    """Check that users enter the correct unit, accept different
    units based on previous answers"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # Check if the response is the entire work
            if response == item:
                return item

        print(f"Please choose a valid option, eg {valid_answers}")


# Main Routine goes here

print()
print(make_statement("Recipe", "🥞"))
print()

want_instructions = yes_no("Do you want to read the instructions? ").lower()

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

name = not_blank("Enter your recipe name: ")
print()

num_check("Serving Size? ")

# loop starts here
while True:
    item_name = not_blank("Ingredient needed: ")

    if item_name == "xxx":
        break

    amount_needed = num_check("Amount needed? ")
    unit_needed = string_check("Unit? ")


print()
print("Let's go shopping or say something.")
amount_to_buy = num_check("Amount in supermarket? ")
unit_to_buy = string_check("Unit? ")
print()
cost_needed = num_check("Cost? ")

# end of loop

# pandas goes here
