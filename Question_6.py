#qestion_6

def apply_function(fun,lst):
	return [fun(x) for x in lst]

print(apply_function(lambda x:x+10,[1,2,3,4]))
