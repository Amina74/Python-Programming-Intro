print("Enter some integres.")

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
c= int(input("Enter an integer: "))
d = int(input("Enter an integer: "))


if a == b or b == c or c == d or d == a:
    print("Duplicates have been found.")
else:
    print("No duplicates")    
