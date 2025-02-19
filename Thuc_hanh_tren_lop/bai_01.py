# Nhập thông tin sinh viên
ma_sv = input("Nhập mã số sinh viên: ")
ho_ten = input("Nhập họ và tên: ")
que_quan = input("Nhập quê quán: ")
nam_sinh = int(input("Nhập năm sinh: "))
diem_tb = float(input("Nhập điểm trung bình các năm học: "))
# Xuất thông tin sinh viên
print("\nThông tin sinh viên:")
print(f"Mã số sinh viên: {ma_sv}")
print(f"Họ và tên: {ho_ten}")
print(f"Quê quán: {que_quan}")
print(f"Năm sinh: {nam_sinh}")
print(f"Điểm trung bình: {diem_tb:.2f}")
