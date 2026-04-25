n = int(input())
m = int(input())

INF = float('INF')

dist = [[INF]* (n+1) for _ in range(n+1)]

for i in range(1,n + 1):
	dist[i][i] = 0

for _ in range(m):
	u,v,w = list(map(int,input().split()))
	dist[u][v] = w

for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			if(dist[i][k] != INF and dist[k][j] != INF):
				dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

for i in range(1,n+1):
	for j in range(1,n+1):
		if dist[i][j] == INF:
			print('INF',end =' ')
		else:
			print(dist[i][j], end= ' ')
	print()