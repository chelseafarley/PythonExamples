from traceback import print_tb


valid_option_entered = False

while not valid_option_entered:
    number = int(input("Enter a number between 1 and 10 (inclusive): "))

    if number >= 1 and number <= 10:
        valid_option_entered = True
        print(f"Option entered: {number}")