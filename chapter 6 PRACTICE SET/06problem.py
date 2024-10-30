# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

student_marks = int(input("Enter your marks: "))

if student_marks>100:
    print("Invalid marks")

elif student_marks>= 90:
    print(f"Your grade is: Ex")

elif student_marks>=80 and student_marks<=90 :
    print(f"Your grade is: A")

elif student_marks>=70 and student_marks<=80 :
    print(f"Your grade is: B")

elif student_marks>=60 and student_marks<=70 :
    print(f"Your grade is: C")

elif student_marks>=50 and student_marks<=60 :
    print(f"Your grade is: D")

elif student_marks<=50 :
    print(f"Your grade is: F")