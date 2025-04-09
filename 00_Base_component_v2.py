# from datetime import date
import pandas
# from tabulate import tabulate


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

 ℹ️ Instructions ℹ️

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

WORK ON THE INSTRUCTIONS!!!!

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
    all_price = []
    all_amount_buy = []
    all_unit_buy = []
    all_cost = []

    # expenses dictionary
    recipe_dict = {
        "Ingredients": all_ingredients,
        "Amount": all_amounts,
        "Unit": all_units,
        "Price": all_price,
        "Buying amount": all_amount_buy,
        "unit for buying": all_unit_buy,
        "Cost": all_cost
    }

    # loop to get expenses
    while True:
        item_name = not_blank("Ingredient needed: ")

        if item_name == "xxx":
            break

        all_ingredients.append(item_name)

    # make panda
    recipe_frame = pandas.DataFrame(recipe_dict)

    # calculate cost to make
    recipe_frame['Cost to make'] = recipe_frame['Price']/recipe_frame['Buying Amount'] * recipe_frame['Amount']

    # return all items for now so we can check loop
    return all_ingredients


def string_check(question, unit_answers):
    """Check that users enter the correct unit, accept different
    units based on previous answers"""

    while True:
        response = input(question).lower()

        for item in unit_answers:

            # Check if the response is the entire work
            if response == item:
                return item

        print(f"Please choose a valid option, eg {unit_answers}")


unit_answers = ["kg", "g", "ml", "l", "tbl", "tablespoon", "cups", "teaspoon", ""]
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

serving_size = num_check("Serving Size? ")

# loop starts here
while True:
    print("Let's start baking...")
    item_name = not_blank("Ingredient needed: ")

    if item_name == "xxx":
        break

    amount_needed = num_check("Amount needed? ")
    unit_needed = string_check("Unit? ", unit_answers)


print()
# end of loop
at_home_ingredients = yes_no("Do you have any ingredients at home? ")
if at_home_ingredients == "yes":
    while True:
        home_ingredient = string_check("Which Ingredient do you have at home? ", valid_answer)
        if home_ingredient == "xxx":
            break

elif at_home_ingredients == "no":
    print()
    print("Let's go shopping!")
    while True:
        ingredient_buying = not_blank("Ingredient?", )
        amount_to_buy = num_check("Amount your buying : ")
        unit_to_buy = string_check("Unit? ", unit_answers)
        print()
        cost_needed = num_check("Cost? ")

print()

# pandas goes here


print("to do, make the panda, write better instruction"
      "finish figuring out the loop")
print("ask the ingredient first, the amount their buying it in, the unit, the amount "
      "the need, the unit, the price")
print("OR the ingredient, the amount they need, the unit, the amount their buying"
      "the unit, the price.")
print("use draw.io to make the two different loops and document")
print("Figure out THE PANDA")
