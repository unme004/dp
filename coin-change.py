val = int(input())
n = int(input())
coins = list(map(int,input().split()))

dp = [0] * (val + 1)
dp[0] = 1

for coin in coins:
	for i in range(coin, val + 1):
		dp[i] += dp[i - coin]

print(dp[val])