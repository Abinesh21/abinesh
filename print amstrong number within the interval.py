a,b=input().split( )
x=int(a)
y=int(b)
for num in range(x,y+1):
	power=len(str(num))
	sum=0
	temp=num
	while temp>0:
		digit=temp%10
		sum=sum+digit**power
		temp//=10
	if num==sum:
		print(num)
