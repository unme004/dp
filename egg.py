eggs = int(input())
floors = int(input())

dp = [[0]* (eggs + 1) for _ in range(floors + 1)]

m = 0
while dp[m][eggs] < floors:
	m+=1
	for e in range(1,eggs + 1):
		dp[m][e] = 1 + dp[m-1][e-1] + dp[m-1][e]

print(m)