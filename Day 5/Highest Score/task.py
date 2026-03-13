student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


max_number = student_scores[0]

for number in student_scores:
    if max_number < number:
        max_number = number

print(max_number)
