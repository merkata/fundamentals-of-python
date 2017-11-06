def ex15(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
                j = i
        else:
            i = k
    print("i =", i, "j =", j, "k =", k)


if __name__ == '__main__':
    i, j, k = 3, 5, 7
    ex15(i, j, k)
    i, j, k = 3, 7, 5
    ex15(i, j, k)
    i, j, k = 5, 3, 7
    ex15(i, j, k)
    i, j, k = 5, 7, 3
    ex15(i, j, k)
    i, j, k = 7, 3, 5
    ex15(i, j, k)
    i, j, k = 7, 5, 3
    ex15(i, j, k)
