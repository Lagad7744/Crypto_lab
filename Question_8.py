#question8

words=["java","python","C","programmer","dog"]

common=[]
for i in range(len(words)):
	for j in range(i+1,len(words)):
		if set(words[i]) & set(words[j]):
			common.append(words[i])
			common.append(words[j])

common=list(set(common))
print(common)
