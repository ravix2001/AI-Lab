# WAP program to get the largest number from a list.

numbers = []
count = 0

while True:
    temp = int(input("Enter a number: "))
    numbers.append(temp)
    count = count+1
    again = input("press enter to add more and 'n' to finish ").lower()
    if again =="n":
        break

print("\nNumbers in list are: ")
for i in range(count):
    print(numbers[i])

largest = numbers[0]

for value in numbers:
    if value > largest:
        largest = value

print("Largest number is : ", largest)