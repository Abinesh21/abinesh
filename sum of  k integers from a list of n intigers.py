n=int(input())
k=int(input())
a=[]
for i in range (n):
	numbers=int(input())
	a.append(numbers)
	b=a[:k]
print(sum (b))
