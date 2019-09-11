def toys(index, nums, k):
    if k <= 0:
        return 0
    
    if index > len(nums)-1:
        return 0

    count = 0
    
    count = max(1 + toys(index + 1, nums, k - nums[index]), toys(index + 1, nums, k))
    return count
    
def solution():
    t = int(input())
    
    while t>0:
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        toys_c = toys(0, nums,k)
        print(toys_c)
        t -= 1

solution()