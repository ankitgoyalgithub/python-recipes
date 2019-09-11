def min_coins(coins, amount):
    num_coins = len(coins)

    t = [[0 if col == 0 else float("inf") for col in range(amount+1)] for _ in range(len(coins))]
    
    for i in range(num_coins):
        for j in range(1, amount+1):
            if j >= coins[i]:
                t[i][j] = min(t[i-1][j], t[i][j-coins[i]]+1)
            else:
                t[i][j] = t[i-1][j]
    
    # Get the Coins Used
    j = amount
    i = num_coins - 1 
    used_coins = list()
    while j > 0:
        if i == 0:
            used_coins.append(coins[i])
            j -= coins[i]
        else:
            if t[i][j] == t[i-1][j]:
                i = i - 1
            else:
                used_coins.append(coins[i])
                j -= coins[i]
    
    for x in t:
        print(x)
    return used_coins, t[num_coins-1][amount]

def count_ways(coins, num_coins, amount):
    if amount == 0:
        return 1
    
    if amount <= 0:
        return 0

    if num_coins <= 0 and amount >= 1:
        return 0
    
    return count_ways(coins, num_coins-1, amount) + count_ways(coins, num_coins, amount - coins[num_coins-1])

def coin_change(amount, coins, num_coins):
    if amount == 0:
        return 0
    
    if amount < 0:
        return 99999

    ans = 99999
    for i in range(num_coins):
        num = coin_change(amount-coins[i], coins, num_coins) + 1

        if num < ans:
            ans = num
    return ans

if __name__ == '__main__':
    coins = [1,5,6,8]
    amount = 7
    print(min_coins(coins, amount))
    print("Number of Solutions:", count_ways(coins, len(coins), amount))
    print("Recursive:", coin_change(amount, coins, len(coins)))