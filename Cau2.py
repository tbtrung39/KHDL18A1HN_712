# Câu 2. Toán tử so sánh
# a) Kiểm tra xem hai số nhập vào có bằng nhau không.
# b) Kiểm tra xem số thứ nhất có lớn hơn số thứ hai không.
# c) Kiểm tra xem số đó có nhỏ hơn 100 hay không.

# a)
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if a == b:
    print("Hai số bằng nhau.")
else:
    print("Hai số không bằng nhau.")
print()

# b)
if a > b:
    print("Số thứ nhất lớn hơn số thứ hai.")
else:
    print("Số thứ nhất không lớn hơn số thứ hai.")
print()

# c)
n = int(input("Nhập một số để kiểm tra: "))
if n < 100:
    print(f"Số {n} nhỏ hơn 100.")
else:
    print(f"Số {n} không nhỏ hơn 100.")
