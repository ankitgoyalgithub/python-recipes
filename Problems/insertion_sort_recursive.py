import random

def insertion_sort_rec(arr, i):
    if i == 0:
        return
    
    insertion_sort_rec(arr, i-1)

    j = i

    while (j > 0) and (arr[j-1] > arr[j]):
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while (j > 0) and (arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    

    
if __name__ == '__main__':
    arr1 = [random.randrange(1000) for i in range(700)]
    insertion_sort_rec(arr1, len(arr1) - 1)
    print(arr1)
    arr2 = [random.randrange(100) for i in range(10)]
    insertion_sort(arr2)
    print(arr2)

