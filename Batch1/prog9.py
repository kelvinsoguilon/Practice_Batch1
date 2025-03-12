#print all number from 0 to 100
even_number = []
for i in range(100):
    if i % 2 == 0:
        even_number.append(i)

print("The even numbers from 0 to 100 are:", even_number)