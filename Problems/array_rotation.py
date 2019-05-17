def left_rotate(arr, N):
    if not arr:
        return arr
    L = len(arr)
    return [arr[i%L] for i in range(N, N+L)]

def right_rotate(arr, N):
    if not arr:
        return arr
    L = len(arr)
    return [arr[(L - i%L)%L] for i in range(N + L, N, -1)]

if __name__ == '__main__':
    test = [1,2,3,4,5]
    print(left_rotate(test,3))
    print(right_rotate(test,2))
