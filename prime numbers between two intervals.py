a,b=input().split( )
x=int(a)
y=int(b)
for num in range(x+1,y):
	if(num>1):
		for i in range(2,num):
			if(num%i==0):
				break
		else:
			print(num)
			
