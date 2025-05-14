# Câu 11. Toán tử số học
# a) Nhập ba số thực và tính trung bình cộng của chúng.
# b) Kiểm tra xem tổng của ba số có lớn hơn 100 hay không.

# a)
a = float(input("Nhập số thực thứ nhất: "))
b = float(input("Nhập số thực thứ hai: "))
c = float(input("Nhập số thực thứ ba: "))
trung_binh = (a + b + c) / 3
print(f"Trung bình cộng của ba số là: {trung_binh:.2f}")
print()

# b)
if (a + b + c) > 100:
    print(f"Tổng của ba số {a}, {b}, {c} lớn hơn 100.")
else:
    print(f"Tổng của ba số {a}, {b}, {c} không lớn hơn 100.")
