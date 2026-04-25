n = int(input())
keys = list(map(int,input().split()))
freq = list(map(int,input().split()))

pre = [0]*(n+1)

for i in range(n):
	pre[i+1] = pre[i] + freq[i]

def sum(i,j):
	return pre[j+1] - pre[i]

def solve(i,j):
	if i > j: return 0
	return min(solve(i,w-1) + solve(w+1,j) for w in range(i,j+1)) + sum(i,j)

print(solve(0,n-1))