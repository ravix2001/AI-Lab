# WAP to calculate the factorial of an input number.

def factorial(n):
    if n == 0 and n==1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
