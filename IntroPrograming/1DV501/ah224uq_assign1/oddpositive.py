import random

generated_number = random.randint(-10,10)
print("The generated number is ", generated_number)


if generated_number% 2 == 0:

    if generated_number >= 0:
        print(generated_number, " is Even number and positive")
    else:
        print(generated_number, "is even number and negative")

else:

    if generated_number >= 0:
        print(generated_number, " is odd number and Positive")
    else:
        print(generated_number, "is odd number and Negative")
