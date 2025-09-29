a=int(input("Enter how many Row : "))
n=int(a/2)
for i in range(1,n+1):
	for j in range(1,i+1):
		print(" * ",end=" ")
	print()
for i in range(n+2,1,-1):
	for j in range(i,1,-1):
		print(" * ",end=" ")
	print()	
