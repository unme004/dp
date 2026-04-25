n = int(input())
words = set(input().split())
s = input()
length = len(s)

dp = [0]*(length + 1)
dp[0]=1

for i in range(1, length + 1):
	for j in range(i):
		if s[j:i] in words:
			dp[i] = 1
			break

print(dp[length])