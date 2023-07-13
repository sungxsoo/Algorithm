def min_coins(n, coins, k):
    dp = [0] + [float('inf')] * k
    for coin in coins:
        for i in range(coin, k+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[k] if dp[k] != float('inf') else -1

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
print(min_coins(n, coins, k))
