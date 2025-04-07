students = {}
while True:
    student_id = input("Nhập số báo danh (hoặc 'q' để thoát): ")
    if student_id == 'q':
        break
    name = input("Nhập họ và tên: ")
    score = float(input("Nhập điểm thi: "))
    students[student_id] = {'name': name, 'score': score}

search_id = input("Nhập số báo danh để tra cứu: ")
if search_id in students:
    print(f"Họ và tên: {students[search_id]['name']}, Điểm thi: {students[search_id]['score']}")
else:
    print("Không tìm thấy thí sinh. Thêm thông tin vào từ điển.")
    name = input("Nhập họ và tên: ")
    score = float(input("Nhập điểm thi: "))
    students[search_id] = {'name': name, 'score': score}