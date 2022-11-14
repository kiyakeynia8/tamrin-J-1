s1 = int(input("input number 1: "))
s2 = int(input("input number 2: "))
s3 = int(input("input number 3: "))

if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
    print("false")

else:
    print("true")