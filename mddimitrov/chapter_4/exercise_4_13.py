def one_to_hundred():
    """
    Asks the user to input number from 1 to 100 inclusive.
    If the number is in this range, print "OK;",
    otherwise do not print anything.
    """
    number = int(input("Please enter a number from 1 to 100: "))
    if number >= 1 and number <= 100:
        print("OK;")
    else:
        print("Out of range.")


if __name__ == '__main__':
    one_to_hundred()
