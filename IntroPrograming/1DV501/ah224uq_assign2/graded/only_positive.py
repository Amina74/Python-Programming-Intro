#number = int(input("Enter a positive number to run a negative number to stop"))
number = 1
count = 0
numbers = []

while True:
    n = int(input("Type a number"))
    if n > 0:
        count += 1
    elif n < 0:
        numbers.append(n)
    elif n == 0:
        print("Well done")
        break

print(numbers)        
print("All positive number are ", count)
print("Enter positive integers. End by giving a negative integer.")

i = 1

positives = []

n = int(input("Integer "+str(i)+": "))

while n>=0:
    positives.append(n)

    i += 1
    
    n = int(input("Integer " + str(i) + ": "))

print()

print("Number of positive integers:", len(positives))
print("Positive numbers:", positives)