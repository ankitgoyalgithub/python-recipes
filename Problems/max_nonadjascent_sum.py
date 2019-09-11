# https://practice.geeksforgeeks.org/problems/stickler-theif/0

def solution(arr, n):
    temp_arr = [0] * n

    temp_arr[0] = arr[0]
    temp_arr[1] = max(arr[0], arr[1])

    for i in range(2, n, 1):
        if temp_arr[i-1] > (arr[i] + temp_arr[i-2]):
            temp_arr[i] = temp_arr[i-1]
        else:
            temp_arr[i] = arr[i] + temp_arr[i-2]
    
    return temp_arr[-1]


if __name__ == '__main__':
    n = 3
    arr = [1,2,3]
    print(solution(arr, n))