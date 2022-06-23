user_entry = int(input("Enter a positive intger: "))
for i in range(1,user_entry+1,2):
    print(i,end=" ")
if user_entry < 0:
    print("Not a valid entry")
