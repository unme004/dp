n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=[[0]*m for _ in range(n)]

dirs=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

for i in range(n):
    for j in range(m):
        for dx,dy in dirs:
            x,y=i+dx,j+dy
            while 0<=x<n and 0<=y<m:
                if a[x][y]==1:
                    ans[i][j]+=1
                    break
                x+=dx; y+=dy

for row in ans:
    print(*row,end=' \n')
