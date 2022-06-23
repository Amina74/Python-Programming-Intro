n = int(input("Enter a positive integer"))
sum, k = 0, 0
if n < 1:
    print("Please enter a value above 1")

else:
    if sum < n:
        k += 2
        sum += k
    print(k, " is the largest k such that 0+2+4+6+...+k <  ", n)
    #
n = int(input("Give a positive integer: "))

sum, k = 0, 0

while sum < n:
    k += 2
    sum += k

print(k-2, "is the largest K such that 0+2+4+6+...+K <", n)
# print(k,"largest K such that 0+2+4+6+...+K < ", n)
