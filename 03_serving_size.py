# check that users enter an integer
# that is more than 13
def num_check(question):
    while True:
        error = "Please enter an integer that is more than 0."

        try:
            response = int(input("Serving Size: "))

            # check that the number is more than / equal to 13
            if response < 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine goes here

# loop for testing purposes


while True:

    print()
    test = num_check("Serving Size: ")