#print all num to 100 except ends in 0
num = []
for i in range(100):
    if i % 10 != 0:
        num.append(i)

print(num)