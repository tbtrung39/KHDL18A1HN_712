# Câu 5. Chuyển đổi kiểu dữ liệu
# a) Nhập một số nguyên và chuyển thành số thực.
# b) Nhập một số thực và chuyển thành số nguyên.
# c) Nhập một số và kiểm tra kiểu của nó.

# a.
n = int(input("Nhập một số nguyên: "))
n_float = float(n)
print("Số sau khi chuyển thành số thực là:", n_float)
print("Kiểu dữ liệu của nó là:", type(n_float))

# b.
x = float(input("Nhập một số thực: "))
x_int = int(x)
print("Số sau khi chuyển thành số nguyên là:", x_int)
print("Kiểu dữ liệu của nó là:", type(x_int))

# c.
s = input("Nhập một số: ")

# Cố gắng chuyển đổi kiểu và kiểm tra
if '.' in s:
    s = float(s)
    print("Đây là số thực.")
elif s.isdigit():
    s = int(s)
    print("Đây là số nguyên.")
else:
    print("Không phải số hợp lệ.")

print("Kiểu dữ liệu sau khi chuyển là:", type(s))
