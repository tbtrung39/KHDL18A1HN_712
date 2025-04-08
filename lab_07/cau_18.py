thisinh = {
    "123": ("Nguyen Van A", 8.5),
    "456": ("Tran Thi B", 9.0)
}

sbd = input("Nhập số báo danh cần tra cứu: ")

if sbd in thisinh:
    ten, diem = thisinh[sbd]
    print(f"Họ tên: {ten}, Điểm thi: {diem}")
else:
    ten = input("Nhập họ và tên thí sinh: ")
    diem = float(input("Nhập điểm thi: "))
    thisinh[sbd] = (ten, diem)
    print("Đã thêm thí sinh mới.")
