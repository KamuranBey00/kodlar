
def sum_of_the_squares(limit1):
    total1 = 0
    for i in range(1,limit1+ 1):
        total1 += i**2 
    return total1

def square_of_the_sums(limit2):
    total2 = 0
    for j in range(1,limit2 +1):
        total2+= j
    total3 = total2 **2
    return total3

result = square_of_the_sums(100)-sum_of_the_squares(100)
print(result)