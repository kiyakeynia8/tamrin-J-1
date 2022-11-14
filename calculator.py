import math

n = float(input("enter first number: "))

print("welcome to my calculator:)")
print("the operation:")
print("+ ","-","*","/","sqr","fac","sin","cos","tan","cot")

op = input()

if op == "sqr":
    k = math.sqrt(n)
    print(k)
    exit()        

if op == "fac":
    k = math.factorial(n)
    print(k)
    exit()
    
if op == "sin":
    n = math.radians(n)
    k = math.sin(n)
    print(k)
    exit()

if op == "cos":
    n = math.radians(n)
    k = math.cos(n)
    print(k)
    exit()

if op == "tan":
    n = math.radians(n)
    k = math.tan(n)
    print(k)
    exit()

if op == "cot":
    n = math.radians(n)
    k = math.atan(n)
    print(k)
    exit()
    
else:
    n2 = float(input("enter second number: "))        
    
    if op == "+":
        x = n + n2
        print(x)

    if op == "-":
        x = n - n2
        print(x)

    if op == "/":
        x = n / n2
        print(x)

    if op == "*":
        x = n * n2
        print(x)