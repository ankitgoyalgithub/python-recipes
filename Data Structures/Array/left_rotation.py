def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(a, b%a)

def left_rotation(nums, d):
    if len(nums) == 0:
        return
    elif len(nums) == 1:
        return nums
    elif d == 0:
        return nums
    else:
        g_c_d = gcd(d%len(nums), len(nums))

        for i in range(g_c_d):
            temp = nums[i]
            j = i
            while True:
                k = j + d

                if k >= len(nums):
                    k -= len(nums)
                
                if k == i:
                    break
                
                nums[j] = nums[k]
                j = k
            nums[j] = temp

def right_rotation(nums, d):
    if len(nums) == 0:
        return
    elif len(nums) == 1:
        return nums
    elif d == 0:
        return nums
    else:
        g_c_d = gcd(d%len(nums), len(nums))

        for i in range(g_c_d):
            temp = nums[len(nums)-1-i]
            j = len(nums) - i - 1
            while True:
                k = j - d

                if k <= 0:
                    k += len(nums)
                
                if k == i:
                    break
                
                nums[j] = nums[k]
                j = k
            nums[j] = temp


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    left_rotation(nums,3)
    print(nums)
    nums = [1,2,3,4,5,6,7,8]
    left_rotation(nums,4)
    print(nums)
    nums = [1,2,3,4,5,6,7,8,9]
    right_rotation(nums,3)
    print(nums)
    nums = [1,2,3,4,5,6,7,8]
    right_rotation(nums,4)
    print(nums)