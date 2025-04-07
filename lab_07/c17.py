# Thông tin mỗi sinh viên gồm: mã sinh viên, tên, điểm (0–10)
students = []

def nhap_sinh_vien():
    ma_sv = input("Nhập mã sinh viên: ")
    ten_sv = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm sinh viên (0–10): "))
    students.append({"ma_sv": ma_sv, "ten_sv": ten_sv, "diem": diem})

def hien_thi_sinh_vien():
    sorted_list = sorted(students, key=lambda x: x["diem"], reverse=True)
    print("\nDanh sách sinh viên sắp xếp theo điểm giảm dần:")
    for sv in sorted_list:
        print(sv)

# Demo
n = int(input("Nhập số lượng sinh viên: "))
for _ in range(n):
    nhap_sinh_vien()

hien_thi_sinh_vien()
