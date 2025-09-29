n1=int(input("Enter the first no for GCD : "))
n2=int(input("Enter the Second no for GCD : "))
if(n1<=n2):
	a=n1
else:
	a=n2
flag=1
for i in range(a,2,-1):
	if(n1%i==0 and n2%i==0):
		print("GCD of ",n1," and ",n2," is : ",i)
		flag=0;
		break

if(flag):
	print("GCD of ",n1," and ",n2," is : ",1)
	
		
