#Câu 1:
# Nhập thông tin sinh viên
ma_so = input("Nhập mã số sinh viên: ")
ho_ten = input("Nhập họ và tên sinh viên: ")
que_quan = input("Nhập quê quán: ")
nam_sinh = int(input("Nhập năm sinh: "))
diem_nam_1 = float(input("Nhập điểm trung bình năm thứ nhất: "))
diem_nam_2 = float(input("Nhập điểm trung bình năm thứ hai: "))
diem_nam_3 = float(input("Nhập điểm trung bình năm thứ ba: "))
# In ra thông tin sinh viên 
print("--- Thông tin sinh viên ---")
print("Mã số:", ma_so)
print("Họ và tên:", ho_ten)
print("Quê quán:", que_quan)
print("Năm sinh:", nam_sinh)
print("Điểm trung bình các năm học:")
print("Năm 1:", diem_nam_1)
print("Năm 2:", diem_nam_2)
print("Năm 3:", diem_nam_3)