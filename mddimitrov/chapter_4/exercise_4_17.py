def ex17_first(n=0):
    if n < 1000:
        print('*', end='')
    if n < 100:
        print('*', end='')
    if n < 10:
        print('*', end='')
    if n < 1:
        print('*', end='')
    print()


def ex17_second(n=0):
    if n < 1000:
        print('*', end='')
    elif n < 100:
        print('*', end='')
    elif n < 10:
        print('*', end='')
    elif n < 1:
        print('*', end='')
    print()


if __name__ == '__main__':
    print("First program 0")
    ex17_first(0)
    print("Second program 0")
    ex17_second(0)
    print("First program 1")
    ex17_first(1)
    print("Second program 1")
    ex17_second(1)
    print("First program 5")
    ex17_first(5)
    print("Second program 5")
    ex17_second(5)
    print("First program 50")
    ex17_first(50)
    print("Second program 50")
    ex17_second(50)
    print("First program 500")
    ex17_first(500)
    print("Second program 500")
    ex17_second(500)
    print("First program 5000")
    ex17_first(5000)
    print("Second program 5000")
    ex17_second(5000)
