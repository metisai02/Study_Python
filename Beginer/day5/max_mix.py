student_heights = input("imput ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

max = student_heights[0]

for i in range(1, len(student_heights)):
    if student_heights[i] > max:
        max = student_heights[i]
print(max)