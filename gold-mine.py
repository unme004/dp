n,m=map(int,input().split())
arr=list(map(int,input().split()))

g = [arr[i*m:(i+1)*m] for i in range(n)]

for j in range(m-2,-1,-1):
	for i in range(n):
		r = g[i][j+1]
		ru = g[i-1][j+1] if i > 0 else 0
		rd = g[i+1][j+1] if i < n -1 else 0
		g[i][j] += max(r,ru,rd)

print(max(row[0] for row in g))