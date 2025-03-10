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


def instructions(yes_no):
    print("ℹ️ Instructions ℹ️")

    print('''

Instructions go here


    ''')
    if want_instructions == "yes" or want_instructions == "y":
        print("Instructions go here")
        print("program continues")
        print()
    elif want_instructions == "no" or want_instructions == "n":
        print("<program continues>")
    else:
        print("please answer yes / no")


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

# Program main heading
print("")

# Ask user if they want to see the instructions
# display as necessary
print()
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()