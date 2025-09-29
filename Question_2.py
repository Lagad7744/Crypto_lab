#Write the program to check if  list has any duplicate element using the set

nums=[1,2,3,4,2,5,6,3]
s={0}
for i in range(len(nums)):
	s.add(nums[i])

if(len(nums)==len(s)):
	print("No duplicate element in the list")
else:
	print("There is duplicate element in ths list")
	
