V=int(input())
E=int(input())
g=[[0]*V for _ in range(V)]
for _ in range(E):
	u,v=map(int,input().split())
	g[u][v]=g[v][u]=1
M=int(input())
c=[0]*V
def ok(u,x):
	for i in range(V):
		if g[u][i] and c[i]==x:
			return 0
	return 1
def f(u):
	if u==V: return 1
	for x in range(1,M+1):
		if ok(u,x):
			c[u]=x
			if f(u+1): return 1
			c[u]=0
	return 0
if f(0):
	print("Solution exists")
else:
	print("Solution does not exist")
