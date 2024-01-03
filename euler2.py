n = int(input("Please Enter the limit of your Fibonacci sequence: "))

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)

sum1 = 0
for i in fibonacci_sequence:
    if i % 2 == 0:
        sum1 += i

print("Sum of even Fibonacci numbers:", sum1)
