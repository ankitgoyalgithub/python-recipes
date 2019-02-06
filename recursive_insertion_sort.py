def insertion_sort(data, index):
    if index == 0:
        return 

    insertion_sort(data, index - 1)

    j = index

    while j > 0 and data[j-1] > data[j]:
        data[j-1], data[j] = data[j], data[j-1]
        j -= 1


if __name__ == "__main__":
    data = [2, 3, 1, 9, 3, 7, 2, 3, 8, 8, 9, 5, 6]
    insertion_sort(data, len(data) - 1)
    print(data)