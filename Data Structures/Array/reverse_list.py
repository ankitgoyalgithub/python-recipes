def reverse(l):
    n = len(l)

    p = 0
    q = n - 1

    while p < q:
        l[p], l[q] = l[q], l[p]
        p += 1
        q -= 1

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    reverse(a)
    print(a)
