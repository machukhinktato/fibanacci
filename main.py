def fibanacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibanacci(n - 1) + fibanacci(n - 2)


if __name__ == '__main__':
    print(fibanacci(5))
    print(fibanacci(6))
    print(fibanacci(7))