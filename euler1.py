x = int(input("Please choose the limit:"))
total = 0
for i in range(x):
    if i % 3 == 0:
        total+= i
for j in range(x):
    if j % 5 == 0:
        total+= j
print(total)