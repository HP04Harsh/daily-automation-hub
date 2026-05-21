a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x,y):
    if y==0:
        return x
    return gcd(y, x % y)

def lcm(x,y):
    return (x*y) // gcd(x,y)

print("GCD of", a, "and", b, "is", gcd(a,b))
print("LCM of", a, "and", b, "is", lcm(a,b))    
