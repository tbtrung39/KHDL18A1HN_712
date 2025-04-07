heights = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
           162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

num_students = len(heights)

average_height = sum(heights) / num_students

print("a. Nhóm có", num_students, "sinh viên.")
print("b. Chiều cao trung bình của các sinh viên trong nhóm là:", round(average_height, 2), "cm.")

unique_heights = set(heights)
average_height = sum(heights) / len(heights)

print("c. Các chiều cao khác nhau:", sorted(unique_heights))
print("Chiều cao trung bình của nhóm:", round(average_height, 2), "cm.")