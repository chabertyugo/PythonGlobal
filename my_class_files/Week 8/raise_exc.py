student_number = input("Please enter your student number!")
if len(student_number) < 8:
    raise Exception("Sorry, the student number must be at least 8 digits long.")
