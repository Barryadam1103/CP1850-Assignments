print("GRADE POINTS TO LETTER GRADE")

grade_point = float(input("Enter grade point:   "))
if grade_point >= 4.0:
    letter_grade = ('A+')
elif grade_point <= 4.0 and grade_point >= 3.7:
    letter_grade = ('A')
elif grade_point <= 3.7 and grade_point >= 3.3:
    letter_grade = ('A-')
elif grade_point <= 3.3 and grade_point >= 3.0:
    letter_grade = ('B+')
elif grade_point <= 3.0 and grade_point >= 2.7:
    letter_grade = ('B')
elif grade_point <= 2.7 and grade_point >= 2.3:
    letter_grade = ('B-')
elif grade_point <= 2.3 and grade_point >= 2.0:
    letter_grade = ('C+')
elif grade_point <= 2.0 and grade_point >= 1.7:
    letter_grade = ('C')
elif grade_point <= 1.7 and grade_point >= 1.3:
    letter_grade = ('C-')
elif grade_point <= 1.3 and grade_point >= 1.0:
    letter_grade = ('D+')
elif grade_point <= 1.0 and grade_point >= 0:
    letter_grade = ('D')
elif grade_point < 1.0:
    letter_grade = ('F')

# Get Results
print ("Your letter grade to grade point will be",letter_grade)

