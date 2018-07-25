t = int(input())
for i in  range(t):
	n, m = [int(x) for x in input().split(' ')]
	a = [int(x) for x in input().split(' ')]
	c = 0
	for j in range(n):
		if a[j]%m==0:
			c = c + 1
	print((2**c) - 1)  
