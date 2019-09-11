dp = None
def subset_sum(nums, k):
    global dp
    if len(nums) == 0:
        return []

    dp = [ [False for _ in range(k+1)] for i in range(len(nums)+1)]
    dp[0][0] = True
    len_nums = len(nums)

    for i in range(1, len_nums+1):
        for j in range(0, k+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            elif nums[i-1] == j:
                dp[i][j] = True
            else:
                dp[i][j] = (dp[i-1][j]) or (dp[i-1][j-nums[i-1]])

    for x in range(len(nums)+1):
        print(dp[x])

def print_subsets_rec(nums, i, sum_l, p=[]):
    global dp
    print(p)
    if (i == 0) and (sum_l != 0) and dp[0][sum_l]: 
        p.append(nums[i]) 
        print(p)
        p = []
        return
  
    if (i == 0) and (sum_l == 0):  
        print(p)
        p = []
        return

    if(dp[i-1][sum_l]):
        print_subsets_rec(nums, i-1, sum_l, p) 

    if (sum_l >= nums[i-1]) and (dp[i-1][sum_l-nums[i-1]]):
        p.append(nums[i-1])
        print_subsets_rec(nums, i-1, sum_l-nums[i-1], p)


if __name__ == '__main__':
    nums = [1,2,5,7]
    k = 8
    subset_sum(nums, k)
    print_subsets_rec(nums, 4, 8, [])