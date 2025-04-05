heights = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

# a. Số sinh viên
num_students = len(heights)
print("Số sinh viên:", num_students)

# b. Chiều cao trung bình
average_height = sum(heights) / num_students
print("Chiều cao trung bình:", average_height)

# c. Chiều cao khác nhau
unique_heights = set(heights)
print("Chiều cao khác nhau:", unique_heights)
print("Chiều cao trung bình:", average_height)