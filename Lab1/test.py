import random

print("Enter the range: ")
x = int(input())
y = int(input())

while True:
    r = random.randint(x,y)

    print(r)

    again = input("\nGenerate again? (Y/N): ").lower()
    
    if again =="n":
        break