#write python code to find the top 2 most frequent element in the list

list_nums=[2,3,5,2,3,7,11,2,2]

s={0}
for i in range(len(list_nums)):
	s.add(i);
first=0
second=0
num1=num2=list_nums[0]
for i in range(len(s)):
	a=list_nums.count(i);
	if(a>first):
		first=a
		num1=i
	elif(a>second):
		num2=i
		second=a
	
	
print(num1,"    ",num2)
