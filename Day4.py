# Define a function to calculate the factorial of a number

def factorial(n):
    if(n == 0):
        return 1
    return n*factorial(n-1)

n = int(input('Enter a number: '))
print(factorial(n))
