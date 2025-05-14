# Câu 1.
# Toán tử logic
# a) Kiểm tra xem một số có lớn hơn 10 và nhỏ hơn 50 không.
# b) Kiểm tra xem số có phải là số nguyên dương không.
# c) Kiểm tra xem số có phải là số lẻ và chia hết cho 5 không.

# a.
x = int(input("Nhập một số: "))
if x > 10 and x < 50:
    print("Số nằm trong khoảng (10, 50).")
else:
    print("Số KHÔNG nằm trong khoảng (10, 50).")

# b.
x = int(input("Nhập một số: "))
if x > 0:
    print("Đây là số nguyên dương.")
else:
    print("Đây KHÔNG phải là số nguyên dương.")

# c.
x = int(input("Nhập một số: "))
if x % 2 != 0 and x % 5 == 0:
    print("Số là số lẻ và chia hết cho 5.")
else:
    print("Số KHÔNG thỏa mãn là số lẻ và chia hết cho 5.")
