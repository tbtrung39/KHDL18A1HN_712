# Câu 2. Toán tử số học
# a) Tính tổng của ba số nhập vào.
# b) Tính trung bình cộng của ba số.
# c) Tìm số lớn nhất trong ba số.

# a.
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
tong = a + b + c
print("Tổng của ba số là:", tong)

# b.
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
tbc = (a + b + c) / 3
print("Trung bình cộng của ba số là:", tbc)

# c.
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
max_number = a
if b > max_number:
    max_number = b
if c > max_number:
    max_number = c
print("Số lớn nhất là:", max_number)
