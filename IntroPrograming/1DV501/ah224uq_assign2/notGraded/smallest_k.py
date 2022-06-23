user_entry = int(input("Enter a positive intger: "))
n = 1
s = 1

while s < user_entry:
     n = n + 2
     s = s + n
print("Smallest N is ", n)

if user_entry < 0 :
    print("Not a valid entry")