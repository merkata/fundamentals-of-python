def ex18():
    """Behold the uglyness of Python."""
    values = list(map(lambda x: int(x), input("Please enter five integers: ")
                      .replace(',', '')
                      .split()))
    print("Maximum is {}".format(max(values)))
    print("Minimum is {}".format(min(values)))


if __name__ == '__main__':
    ex18()
