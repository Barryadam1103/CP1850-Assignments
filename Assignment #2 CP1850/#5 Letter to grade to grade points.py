print("LETTER GRADE TO GRADE POINTS")

# Get user input
l_grade = str(input("Enter letter grade:  "))

if l_grade == 'A+':
    grade_p = '4.0'
elif l_grade == 'A':
    grade_p = '4.0'
elif l_grade == 'A-':
    grade_p = '3.7'
elif l_grade == 'B+':
    grade_p = '3.3'
elif l_grade == 'B':
    grade_p = '3.0'
elif l_grade == 'B-':
    grade_p = '2.7'
elif l_grade == 'C+':
    grade_p = '2.3'
elif l_grade == 'C':
    grade_p = '2.0'
elif l_grade == 'C-':
    grade_p = '1.7'
elif l_grade == 'D+':
    grade_p = '1.3'
elif l_grade == 'D':
    grade_p = '1.0'
elif l_grade == 'F':
    grade_p = '0'

# Get results
print("Your letter grade to grade point is", grade_p)


