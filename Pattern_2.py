n=int(input("Enter the row no : "))
for i in range (1,n+1):
	if(i<=n/2):
		for j in range(1,i+1):
			print(" * ",end=" ")
		print()
	elif(i>n/2):
		for k in (n-i+1,n+1):
			print(" * ",k,end=" ")
		print()
			
	
		
