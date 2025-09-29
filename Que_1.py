def extended_gcd(a,b):
	if b==0:
		return a,1,0
	g,x1,y1=extended_gcd(b,a%b)
	return g,y1,x1-(a//b)*y1

def solve(a,b,c):
	g,x,y=extended_gcd(a,b)
	if c%g !=0:
		print("No sloution for that Integer")
		return 
	factor=c//g
	x *=factor
	y *=factor
	print("particular Solution : X =",x,"y= ",y)
	print("General  solution : x =",x ,"+",(b//g),"t , y = ",y,"-",(a//g),"t")
	
	sol=[]
	for t in range(-10,20):
		x0=x+(b//g)*t
		y0=y-(a//g)*t
		
		if(-10<=x0<=20 and -10<=y0<=20):
			sol.append([x0,y0])
	print(sol)
		
print("------------------------------------------------")
print("Equation 56x +72y=40")
solve(56,72,40)

print("-----------------------------------------------")
print("Equation of 24x + 138y=18")
solve(24,138,18)
