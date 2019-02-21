a=int(input())
power=len(str(a))
sum=0
temp=a
while temp>0:
	digit=temp%10
	sum=sum+digit**power
	temp//=10
if (a==sum):
	print('yes')
else:
	print('no')
	
