# Câu 9. Tính toán với số thực
# a) Nhập hai số thực và tính thương của chúng với hai chữ số thập phân.
# b) Kiểm tra xem một số thực nhập vào có phải là số âm không.

# a)
a = float(input("Nhập số thực thứ nhất: "))
b = float(input("Nhập số thực thứ hai: "))
if b != 0:
    thuong = a / b
    print(f"Thương của {a} và {b} là: {thuong:.2f}")
else:
    print("Không thể chia cho 0.")
print()

# b)
n = float(input("Nhập một số thực để kiểm tra: "))
if n < 0:
    print(f"Số {n} là số âm.")
else:
    print(f"Số {n} không phải là số âm.")
