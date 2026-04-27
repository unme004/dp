n,reqSum = map(int,input().split())
arr = list(map(int,input().split()))
ans = []
def subset(currIdx,Sum,c):
	if Sum == reqSum:
		ans.append(c)
		return
	if currIdx == n or Sum > reqSum: return
	subset(currIdx+1,Sum + arr[currIdx],c+[arr[currIdx]])
	subset(currIdx+1,Sum,c)
subset(0,0,[])

if ans:
	for i in ans:
		print('[',end='')
		print(*i,end=']\n')
else:
	print('No subset found')
