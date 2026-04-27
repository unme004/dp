n = int(input())
e = int(input())
adj = [[] for _ in range(n)]

for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [-1]*n
color[0] = 0

for u in range(1, n):
    used = [False]*n
    for v in adj[u]:
        if color[v] != -1:
            used[color[v]] = True

    c = 0
    while used[c]:
        c += 1
    color[u] = c

print(max(color) + 1)
