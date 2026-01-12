# Fibonacci series with user input

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Take input from user
num = int(input("Enter the number of terms: "))

print("Fibonacci series:")
print(fibonacci(num))