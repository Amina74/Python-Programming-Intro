print("Please provide three integers A, B, C")
num_1 = int(input("Enter A:"))
num_2 = int(input("Enter B:"))
num_3 = int(input("Enter C:"))

if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1
elif num_2 >=  num_1 and num_2 >=num_3:
    largest = num_2
else:
    largest = num_3        
print("\nThe largest number is:", largest)    