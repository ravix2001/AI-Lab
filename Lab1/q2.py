# WAP to input the percentage and display the division
# >=80 →  Distinction
# >=65 →  First Division
# >=55 →  Second Division
# >=40 →  Third Division
# <40  →  Fail

def grades(percent):
    if(percent>=0 and percent<=100):
        if(percent>=80):
            print("Distinction")
        elif(percent>=65):
            print("First Division")
        elif(percent>=55):
            print("Second Division")
        elif(percent>=40):
            print("Third Division")
        else:
            print("Fail")
    else:
        print("Please enter in between the range")

percentage = int(input("Enter percentage: "))

grades(percentage)