import sys
n = int(input("Enter an odd positive integer: "))
if (n <= 0) or (n % 2 ==  0):
    print("Enter an odd positive integer again: ")
for i in range(n):
    print(' ' * i + '*' * (n - i))

print("Isosceles Triangle:")
for i in range(1, n + 1, 2):
    space = (n - i) // 2
    print(' ' * space + '*' * i + ' ' * space)    