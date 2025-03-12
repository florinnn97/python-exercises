def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Test
num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is {factorial_recursive(num)}.")
