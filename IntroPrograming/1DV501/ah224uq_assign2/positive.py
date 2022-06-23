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
