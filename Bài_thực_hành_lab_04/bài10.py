# Nhập số nguyên
num = int(input("Nhập một số nguyên dương: "))

# Kiểm tra nếu số âm thì yêu cầu nhập lại
while num < 0:
    num = int(input("Vui lòng nhập số nguyên dương: "))

# Danh sách chữ số
so_chu = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

# Chuyển số thành chuỗi và in từng chữ số
num_str = str(num)
for digit in num_str:
    print(so_chu[int(digit)], end=" ")

print()  # Xuống dòng sau khi in xong
