number = 0
count = 0
numbers = []
print("Enter a positive integer. End by giving a negative")
while True:
    number += 1
    n = int(input("Integer" + str(number) + ": "))
   
    
    
    if n > 0:
        count += 1
        numbers.append(n)
    elif n < 0:
        print()
        break
    
       
print("All positive number are ", count)
print("The positive values: ", numbers) 

