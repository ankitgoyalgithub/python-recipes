def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = int(l + (r - l)/2)
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x:
            if mid-1 < l:
                return mid - 1
            return binarySearch(arr, l, mid-1, x) 
        else: 
            if r < mid + 1:
                return mid
            return binarySearch(arr, mid + 1, r, x)

arr = [ 2, 3, 4, 10, 40 ] 
x = 1
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")