def isPrimeNumber(number):
    if number == 2:
        #print(number, "is a prime number.")
        return True
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                #print(number, "is not a prime number.")
                return False
        #print(number, "is a prime number.")
        return True
    else:
        #print(number, "is not a prime number.")
        return False
    
# Test the function
# input = int(input("Is this number a prime number?\nEnter a number: "))
# isPrimeNumber(input)