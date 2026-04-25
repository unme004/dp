n = int(input())
m = int(input())
items = list(map(int,input().split()))
weights = list(map(int,input().split()))

dp = [0] * (m+1)

for i in range(n):
	for j in range(m, weights[i] - 1, -1):
		dp[j] = max(dp[j], items[i] + dp[j - weights[i]])

print(dp[m])