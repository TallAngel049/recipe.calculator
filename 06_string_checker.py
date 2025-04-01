# Functions go here
def string_check(question, valid_ans_list, num_letters):
    """Check that users enter the full word
    or the 'n' letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # Check if the response is the entire work
            if response == item:
                return item

            # Check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


valid_ans_list = "kg", "g", "ml", "l", "unit"
like_coffee = string_check("Do you like coffee? ")
