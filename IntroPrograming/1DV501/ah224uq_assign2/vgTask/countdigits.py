def count():
    odd, even, zero = 0, 0, 0
    for i in num:
        if i == 0:
            zero += 1
        elif i % 2 == 0:
            even += 1
        else:
            odd += 1
    return zero, even, odd


number = input("Enter a large positive integer:")
num = (int(i) for i in number)

zero, even, odd = count()
print("Zeros:", zero, "\nOdd:", odd, "\nEven:", even)
