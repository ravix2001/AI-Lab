# WAP to check if an input number is odd or even

def check(num):
    if (num % 2) == 0:
        print("even")
    else:
        print("odd")

num = int(input("Enter a number: "))
check(num)  