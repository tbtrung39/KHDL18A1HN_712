# Câu 9. Toán tử logic và so sánh
# a) Nhập hai số nguyên và kiểm tra xem số nào lớn hơn.
# b) Kiểm tra xem một số có thuộc khoảng từ 10 đến 50 hay không.

# a.
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
if a > b:
    print("Số lớn hơn là:", a)
elif b > a:
    print("Số lớn hơn là:", b)
else:
    print("Hai số bằng nhau.")

# b.
n = int(input("Nhập một số: "))
if 10 <= n <= 50:
    print(n, "thuộc khoảng từ 10 đến 50.")
else:
    print(n, "không thuộc khoảng từ 10 đến 50.")
