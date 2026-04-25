def prim_mst(n, graph):
	INF = float('inf')
	
	key = [INF] * n
	parent = [-1] * n
	visited = [False] * n

	key[0] = 0

	for _ in range(n):
		u = -1
		min_val = INF
		for v in range(n):
			if not visited[v] and key[v] < min_val:
				min_val = key[v]
				u = v

		visited[u] = True

		for v in range(n):
			if graph[u][v] != 0 and not visited[v] and graph[u][v] < key[v]:
				key[v] = graph[u][v]
				parent[v] = u

	for i in range(1, n):
		print(f"{parent[i]} - {i} -> {graph[parent[i]][i]} ")

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

print('Edge -> Weight')
prim_mst(n, graph)