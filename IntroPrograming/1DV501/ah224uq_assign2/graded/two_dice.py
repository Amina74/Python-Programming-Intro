import random


def dice():
    return random.randint(1, 6)


# def list():
lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(1, 10001):
    sum = dice() + dice()
    lst[sum - 2] += 1
# return ls
# lst = list()
n = 2
print("Frequency table (sum,count)for rolling two dices for 100000 times:")
for x in lst:
    print(n, "     ", x)
    # print(x + 2, "", ls[x])
    n += 1
