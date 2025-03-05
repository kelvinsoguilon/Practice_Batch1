#odd number
odd_number = []
for i in range(10):
    num = int(input("Enter a number:"))

    if num % 2 == 1:
        odd_number.append(num)

print("The number of odd numbers entered is:", odd_number)