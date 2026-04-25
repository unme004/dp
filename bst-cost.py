n=int(input())
f=list(map(int,input().split()))

pre=[0]*(n+1)
for i in range(n):
	pre[i+1]=pre[i]+f[i]

def s(i,j):
	return pre[j+1]-pre[i]

def solve(i,j):
	if i>j: return 0
	return min(solve(i,r-1)+solve(r+1,j) for r in range(i,j+1)) + s(i,j)

dp=[[0]*n for _ in range(n)]

for i in range(n):
	for j in range(i,n):
		dp[i][j]=solve(i,j)

for i in range(n):
	for j in range(n):
		if j < n-1:
			print(dp[i][j] if i<=j else 0,end=" ")
		else:
			print(dp[i][j] if i<=j else 0,end='')
			
	print()