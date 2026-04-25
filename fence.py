n,k=map(int,input().split())

mod=1000000007

if n==1:
	print(k%mod)
	exit()

same=0
diff=k

for _ in range(2,n+1):
	same,diff=diff,(same+diff)*(k-1)%mod

print((same+diff)%mod)