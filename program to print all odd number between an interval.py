n,q=input().split(' ')
n=int(n)
q=int(q)
for num in range(n+1,q+1):
	if (num%2!=0):
		print(num,end=' ')
