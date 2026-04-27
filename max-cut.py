n=int(input())
a,b,c=map(int,input().split())
dp=[float('-inf')]*(n+1)
dp[0] = 0
for i in range(1,n+1):
	dp[i]=max((dp[i-x]+1 for x in (a,b,c) if i>=x),default=float('-inf'))
print(max(0,dp[n]))
