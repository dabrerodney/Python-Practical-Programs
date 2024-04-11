# Write a program that takes the marks of 5 subjects and displays the grade

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark) 

average = sum(marks) / len(marks)

grade = calculate_grade(average)

print(f"Average marks: {average:.2f}")
print(f"Grade: {grade}")
