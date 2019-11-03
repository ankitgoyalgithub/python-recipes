# https://www.techiedelight.com/sort-array-containing-0s-1s-2s-dutch-national-flag-problem/

def solution(array):
    end = len(array) - 1
    start = 0
    mid = 0
    pivot = 1

    while mid <= end:
        if array[mid] < pivot:
            array[start], array[mid] = array[mid], array[start]
            start += 1
            mid += 1
        elif array[mid] > pivot:
            array[mid], array[end] = array[end], array[mid]
            end -= 1
        else:
            mid += 1

if __name__ == '__main__':
    array = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    solution(array)
    print(array)