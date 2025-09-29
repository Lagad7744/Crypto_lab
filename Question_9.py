#question_9

ls=[1,2,3,2,4,1,5,1,2]
def func(ls):
	ans=[]
	for i in set(ls):
		cnt=ls.count(i)
		if cnt==2:
			ans.append(i)
	return ans
print("the list of number apperaing exactly twice : ",func(ls))
