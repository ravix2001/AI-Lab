# WAP program to sum all the items in a list

data = []
count = 0
sum = 0
while True:
    temp = int(input("Enter a number: "))
    data.append(temp)
    count = count+1
    again = input("press enter to add more and 'n' to finish ").lower()
    if again =="n":
        break
    
print("\nNumbers in list are: ")
for i in range(count):
    print(data[i])

for i in range(count):
    sum = sum + data[i]

print("\nThe sum of numbers in the list is ",sum)