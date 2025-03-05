# functions go here

# main routine goes here

while True:
    want_instructions = input("Do you want to read the instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("Instructions go here")
        print("program continues")
        print()
    elif want_instructions == "no" or want_instructions == "n":
        print("<program continues>")
    else:
        print("please answer yes / no")

