# WAP to calculate sum, diff, product and quotient between two input numbers using a single function

def calculate(x,y):
    sum = x+y
    print("Sum = ", sum)

    diff = x-y
    print("Difference = ", diff)

    prod = x*y
    print("Product = ", prod)

    quotient = x/y
    print("Quotient = ", quotient)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

calculate(num1,num2)