def sum_seq(arr, l):
    if l == 0:
        return 0
    else:
        return arr[l-1] + sum_seq(arr, l-1)


if __name__ == "__main__":
    print(sum_seq([5,4,3,2,6], 5))