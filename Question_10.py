import numpy as np
arr=np.random.randint(1,30,(5,5))
print(arr)
meanvalue=arr.mean()
print(meanvalue)
result=np.where(arr>meanvalue,1,0)

print("Modified Array :\n",result) 
