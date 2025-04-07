#Câu 4:
heights=[161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]
num_students=len(heights)
avg_height=sum(heights)/num_students
unique_heights=sorted(set(heights))
print("a, số lượng sinh viên trong nhóm:",num_students)
print("b, chiều cao trung bình của sinh viên:",round(avg_height,2))
print("c, các chiều cao khác nhau:",unique_heights)