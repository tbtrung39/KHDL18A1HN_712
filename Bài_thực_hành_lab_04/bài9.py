# Nhập số nguyên từ bàn phím
num = int(input("Nhập một số nguyên dương: "))

# Kiểm tra nếu số âm thì yêu cầu nhập lại
while num < 0:
    num = int(input("Vui lòng nhập số nguyên dương: "))

# Tính tổng các chữ số
sum_digits = 0
temp = num

while temp > 0:
    sum_digits += temp % 10  # Lấy chữ số cuối cùng và cộng vào tổng
    temp //= 10  # Bỏ chữ số cuối cùng

# Hiển thị kết quả
print(f"Tổng các chữ số của {num} là: {sum_digits}")
