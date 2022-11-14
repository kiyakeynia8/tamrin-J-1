w = float(input("enter your weight (KG)"))
h = float(input("enter your height (M)"))

BMI = w / h

print("your BMI =", BMI)

if BMI < 18.5:
    print("underheight")

if 18.5 < BMI < 24.9:
    print("normal height")

if 29.9 < BMI < 25:
    print("overheight")

if 30 < BMI < 34.9:
    print("obesllty")

if 35 < BMI < 39.9:
    print("xtreme obeslty")