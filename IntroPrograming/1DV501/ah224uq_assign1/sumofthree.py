a_number = int(input("Provide a three digit number: "))
first_number= a_number // 100
second_number= (a_number //10) % 10
third_number= a_number % 10
sum = first_number + second_number+ third_number
print("Sum of the digits: " , sum)
