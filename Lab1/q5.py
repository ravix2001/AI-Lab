# WAP to enter the marks of 10 students and display it

# Initialize an empty list to store the marks
marks = []
def get_marks():
    for i in range(10):
        while True:
            mark = float(input(f"Enter marks for student {i + 1}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter a value between 0 and 100.")

def show_marks():
    print("\nMarks of 10 students:")
    for i in range(10):
        print(marks[i])

get_marks()
show_marks()