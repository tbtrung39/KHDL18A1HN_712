#câu 18:
students={
    "123":["Nguyễn Văn A",8.5],
    "124":["Trần Thị B",7.0],
    "125":["Lê Văn C",9.2]
}
sbd = input("Nhập số báo danh:")
if sbd in students:
    print(f"thí sinh: {students[sbd][0]}, điểm thi: {students[sbd][1]}")
else:
    name = input("Nhập họ tên thí sinh:")
    score = float(input("Nhập điểm thi:"))
    students[sbd]=[name,score]
    print("thông tin đã được thêm vào danh sách")
print("\n danh sách thí sinh:")
for key,value in students.items():
    print(f"SBD: {key}, họ tên:{value[0]},điểm thi:{value[1]}")