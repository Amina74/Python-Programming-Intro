import random
from typing import Counter
input = int(input("Enter number of integers to be generated: "))



sum = 0
print("\nGenerated values: ", end='')
num = random.randint(1, 100)
max = num
min = num

for numberCount in range(1, input+1):
    num = random.randint(1, 100)
    print(num, "", end='')

    sum += num
    if num < min:
        min = num
    if num > max:
        max = num

print("\nAverage = {:.2f}".format(sum / input),"min =", min, " and max =", max)
