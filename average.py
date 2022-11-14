name = input("enter your name: ")
family = input("enter your family: ")

n1 = int(input("English = "))
n2 = int(input("Math = "))
n3 = int(input("Chemistry = "))

average = (n1 + n2 + n3) / 3

print(average)

if average >= 17:
    print(name, family, "your average is Great")

elif 17 > average >= 12:
    print(name, family, "your average is Normal")

elif average <12:
    print(name, family, "your average is Fail")
