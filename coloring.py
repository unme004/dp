n,m=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(n)]
c=[0]*n
def coloring(u):
	if u==n: return 1
	for x in range(1,m+1):
		if all(not g[u][i] or c[i]!=x for i in range(n)):
			c[u]=x
			if coloring(u+1): return 1
			c[u]=0
	return 0
coloring(0)

print(*c, end=" ")
