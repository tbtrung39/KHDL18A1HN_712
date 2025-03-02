# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương: "))

i = 2  # Bắt đầu từ số nguyên tố nhỏ nhất
print(f"Phân tích số {n} thành thừa số nguyên tố:", end=" ")

# Tìm thừa số nguyên tố
while i * i <= n:
    while n % i == 0:
        print(i, end=" ")  # In thừa số
        n //= i
    i += 1

# Nếu còn lại một số nguyên tố cuối cùng
if n > 1:
    print(n)