n,max_depth=map(int,input().split())
keys=list(map(int,input().split()))
freq=list(map(int,input().split()))


pre=[0]*(n+1)
for i in range(n):
	pre[i+1]=pre[i]+freq[i]

def s(i,j):
	return pre[j+1]-pre[i]

def solve(i,j,d):
	if i>j: return 0
	if d==0: return float('inf')
	return min(
		solve(i,r-1,d-1)+solve(r+1,j,d-1)+s(i,j)
		for r in range(i,j+1)
	)

ans=solve(0,n-1,max_depth)
print(ans if ans!=float('inf') else -1)