def get_subject_with_highest_grade(grades):
    highest_grade = 0
    subject_with_highest_grade = ''

    for subject, grade in grades:
        if grade > highest_grade:
            highest_grade = grade
            subject_with_highest_grade = subject

    return subject_with_highest_grade
grades = [('Англійська мова', 88), ('Біологія', 90), ('Математика', 97), ('Українська мова', 82)]
print(get_subject_with_highest_grade(grades))