from datetime import date
import pandas
from tabulate import tabulate


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
the program will ask you to give the amount, and the price,.

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


def string_check(question, valid_ans):
    while True:
        response = input(question).lower()

        # checks user response
        if response in valid_ans:
            return valid_ans[response]

        else:
            print(f"Please choose a valid option, eg 'kg'.")


def get_ingredients(rec_type):
    """Gets variable / fixed expenses and outputs
    panda (as a sting) and a subtotal of expenses"""

    # Lists for pandas
    ingredient_list = []
    amount_list = []
    unit_list = []

    all_amount_buy = []
    all_unit_buy = []
    price_list = []

    # loop starts here
    while True:
        item_name = not_blank("Ingredient needed: ")

        if item_name == "xxx":
            break

        amount = num_check("Amount needed: ")
        unit = string_check("Unit? ", unit_map)
        print()
        amount_buy = num_check("How much are you buying? ")
        unit_buy = string_check("Unit for buying amount? ", unit_map)
        price = num_check("Price: ")

        ingredient_list.append(item_name)
        amount_list.append(amount)
        unit_list.append(unit)

        # second panda
        all_amount_buy.append(amount_buy)
        all_unit_buy.append(unit_buy)
        price_list.append(price)

    # recipes dictionary
    recipe_dict = {
        "Ingredients": ingredient_list,
        "Amount": amount_list,
        "Unit": unit_list,
        "Buying Amount": all_amount_buy,
        "Buying Unit": all_unit_buy,
        "Price": price_list,
    }

    recipe_frame = pandas.DataFrame(recipe_dict)

    # calculate cost to make
    recipe_frame['Cost to make'] = recipe_frame['Price'] / recipe_frame['Buying Amount'] * recipe_frame['Amount']

    # make expenses frame into a string with the desired columns
    if rec_type == "variable":
        recipes_string = tabulate(recipe_frame, headers='keys', tablefmt='psql', showindex=False)
    else:
        recipes_string = tabulate(recipe_frame[['Ingredients', 'Price']], headers='keys',
                                  tablefmt='psql', showindex=False)

    # return all items
    return recipes_string


# unit map valid ans
unit_map = {
    "kg": "kg",
    "kilogram": "kg",
    "kilograms": "kg",
    "g": "g",
    "gram": "g",
    "grams": "g",
    "ml": "ml",
    "milliliter": "ml",
    "milliliters": "ml",
    "l": "l",
    "litre": "l",
    "litres": "l",
    "tablespoon": "tbl",
    "tbl": "tbl",
    "teaspoon": "tsp",
    "tsp": "tsp",
    "cup": "cups",
    "cups": "cups",
    "c": "cups",
    "": ""
}


# Main Routine goes here


print()
print(make_statement("Recipe Calculator", "🥞"))
print()

# ask users if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions? ").lower()

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

name = not_blank("Enter your recipe: ")
print()

# Checks that users entered a valid serving size
serving_size = num_check("Serving Size? ")

# *** Get current date for heading and filename ***
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Headings / strings
main_heading_string = make_statement(f"Recipe Calculator "
                                     f"({name}, {day}/{month}/{year})", "--")
serving_size_string = f"Serving Size being made: {serving_size}"


# Pandas write to file
recipe_string = get_ingredients("variable")

total_cost_to_make_string = f"Total: HOW DO I DO THIS"
per_serve_string = f"Per Serve: AND THIS????"


# write to file
to_write = [main_heading_string,
            "\n", serving_size_string,
            "\n", recipe_string]

# print area
print()
for item in to_write:
    print(item)

# create file to hold date (add .txt extension)
file_name = f"{name}_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
