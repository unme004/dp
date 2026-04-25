n,W,k = list(map(int,input().split()))
weights = []
values = []

dp = [[0]*(k + 1) for _ in range(W + 1)]

for i in range(n):
	w,v = list(map(int,input().split()))
	weights.append(w)
	values.append(v)

for i in range(n):
	for j in range(W, weights[i] - 1, -1):
		for w in range(k, 0 ,-1):
			dp[j][w] = max(dp[j][w], values[i] + dp[j - weights[i]][w - 1])

print(dp[W][k])