#write a function to flatten this list completely into a single list

flat_nums=[1,2,3,[4,5],(6,7),[8,[9,10]]]
list1=[]
def remove_tuple(l):
	for i in l:
		list1.append(i)
"""
def remove_list_1(l):
	for i in l:
		if(type(i)==list):
			remove_list_1(i)
		elif(type(i)==tuple):
			remove_tuple(i);
		else:
			list1.append(i)
"""		
def remove_list(l):
	for i in l:
		if(type(i)==list):
			remove_list(i)
		elif(type(i)==tuple):
			remove_tuple(i)
		elif(type(i)== int):
			list1.append(i)
remove_list(flat_nums)
print(list1)
