# Nhập hai số nguyên
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

# Tìm số lớn nhất giữa a và b
max_num = max(a, b)

# Tìm BCNN bằng cách tăng dần từ số lớn nhất
while True:
    if max_num % a == 0 and max_num % b == 0:
        bcnn = max_num
        break
    max_num += 1

# In kết quả
print("Bội chung nhỏ nhất là:", bcnn)