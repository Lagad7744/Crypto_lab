def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)
    
a=int(input("Enter the Value a : "))
b=int(input("Enter the Value of b(b!=0) : "))

print("GCD of ",a," and ",b," is : ",GCD(a,b))
