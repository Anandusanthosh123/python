# Check if a number is prime or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
else:
    print(num, "is NOT a prime number")