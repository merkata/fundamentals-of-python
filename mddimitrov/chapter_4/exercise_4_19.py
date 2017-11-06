def ex19():
    """This exercise finds duplicates from a list of integer values.
    Also behold once more :))."""
    values = list(map(lambda x: int(x), input("Please enter five integers: ")
                      .replace(',', '')
                      .split()
                      ))
    print("Values {}".format(values))
    result = "ALL UNIQUE" if all(list(map(
        lambda x: values.count(x) == 1, values))) else "DUPLICATES"
    print(result)


if __name__ == '__main__':
    ex19()
