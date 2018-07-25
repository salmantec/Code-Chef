def prob(n):
	x = int(n/2)
	q = 10**x
	return [1, q]
	
t = int(input("Enter the number of test cases(T): "))
while(t>0): 
	n = int(input("Enter the length of each PIN(N): "))
	p,q = prob(n)
	print(p,"",q)
	t = t-1


