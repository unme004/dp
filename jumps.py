n=int(input())
arr=list(map(int,input().split()))

jumps=end=reach=0

for i in range(n-1):
	if i > reach:
		print(-1)
		exit()
	reach = max(reach, i+arr[i])
	if i == end:
		jumps+=1
		end=reach

print(jumps if reach>=n-1 else -1)