from A04 import isPrimeNumber

def nextPrime(number):
    while True:
        number += 1
        if isPrimeNumber(number):
            print(f"The next prime number after the input is {number}.")
            return number
        else:
            print(f"{number} is not a prime number.")

# Test the function
# input = int(input("Enter a number: "))
# nextPrime(input)