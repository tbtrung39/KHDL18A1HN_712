# Câu 4.
# Làm việc với số
# a)	Nhập hai số nguyên từ bàn phím.
# b)	Tính tổng, hiệu, tích, thương của hai số đó.
# c)	Kiểm tra xem số thứ nhất có chia hết cho số thứ hai không.

# a.
so1 = int(input("Nhập số nguyên thứ nhất: "))
so2 = int(input("Nhập số nguyên thứ hai: "))

# b.
tong = so1 + so2
hieu = so1 - so2
tich = so1 * so2
if so2 != 0:
    thuong = so1 / so2
else:
    thuong = "Không thể chia cho 0"
print(f"Tổng: {tong}, Hiệu: {hieu}, Tích: {tich}, Thương: {thuong}")

# c.
if so1 % so2 == 0:
    print(f"{so1} chia hết cho {so2}")
else:
    print(f"{so1} không chia hết cho {so2}")
