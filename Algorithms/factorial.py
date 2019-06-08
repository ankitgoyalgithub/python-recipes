def fact(n):
    result = 1

    while n > 0:
        result = n * result
        n -= 1
    return result

if __name__ == '__main__':
    print(fact(20000))