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


# main routine goes here
while True:
    name = not_blank("Enter your recipe: ")
    if name == "xxx":
        print("We are done")
        break
