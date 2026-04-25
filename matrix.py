n = int(input())
arr = list(map(int,input().split()))

def solve(i,j):
	if i==j: return 0
	return min(solve(i,k) + solve(k+1,j) + arr[i-1]*arr[k]*arr[j] for k in range(i,j))

print(solve(1,n-1))