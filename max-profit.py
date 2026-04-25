n = int(input())
cost = list(map(int,input().split()))

b1=b2=float('-inf')
s1=s2=0

for x in cost:
	b1=max(b1,-x)
	s1=max(s1,b1+x)
	b2=max(b2,s1-x)
	s2=max(s2,b2+x)

print(s2)