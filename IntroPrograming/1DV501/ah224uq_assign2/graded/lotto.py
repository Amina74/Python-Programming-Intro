import random

print("The Lotto numbers this week: ")
num = []
r = range(1, 35)
count = 7
num = random.sample(r, count)
num.sort()
print(num)
