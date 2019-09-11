def num_ways(coins, value):
    num_coins = len(coins)
    t = [[0 for _ in range(value + 1)] for _ in range(num_coins)]

    for i in range(num_coins):
        for j in range(value+1):
            if j == 0:
                t[i][j] = 1
            else:
                if j >= coins[i]:
                    t[i][j] = t[i-1][j] + t[i][j - coins[i]]
                else:
                    t[i][j] = t[i-1][j]
    return t[num_coins-1][value]

def num_ways_recursive(coins, index, value):
    if value == 0:
        return 1    

    if value < 0:
        return 0

    if index >= len(coins):
        return 0

    return num_ways_recursive(coins, index, value-coins[index]) + num_ways_recursive(coins, index+1, value)

if __name__ == '__main__':
    coins = [3,2,1]
    value = 5
    print(num_ways(coins, value))
    print(num_ways_recursive(coins, 0, 5))