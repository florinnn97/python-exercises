import math

def este_prim(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # check only until sqrt(n)
        if n % i == 0:
            return False
    return True

# Testăm funcția
numar = int(input("Input the number you want to check if it's prime: "))
if este_prim(numar):
    print(f"Number {numar} is prime!")
else:
    print(f"Number {numar} is not prime!")
