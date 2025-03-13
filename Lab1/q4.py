# WAP to display prime numbers from 1 to 100

for number in range (2, 101):
    count = 0
    for i in range(2, (number//2 + 1)):
        if(number % i == 0):
            count = count + 1
            break
    if(count==0):
        print(number, end=' ')