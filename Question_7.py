#question_7

tup1=[(1,2),(3,4),(5,6),(1,2,3)]

tup2=[]
def add_tuple(l):
	a=0
	for i in l:
		a+=i;
	tup2.append(a);
for i in tup1:
	if(type(i)==tuple):
		add_tuple(i)
print(tuple(tup2))
