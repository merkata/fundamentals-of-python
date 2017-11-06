def ex16(val=0):
    """Exercise 16."""
    # val = int(input())
    if val < 10:
        if val != 5:
            print("wow ", end='')
        else:
            val += 1
    else:
        if val == 17:
            val += 10
        else:
            print("whoa ", end='')
    print(val)


if __name__ == '__main__':
    ex16(3)
    ex16(21)
    ex16(5)
    ex16(17)
    ex16(-5)
