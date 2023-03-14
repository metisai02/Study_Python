
student_heights = input("imput ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# sum_heights = sum(student_heights)
# print(round(sum_heights/len(student_heights)))
sum_t = 0
count = 0;
for i in student_heights:
    sum_t += i
    count+=1
print(round(sum_t/count))
